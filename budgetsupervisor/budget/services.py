import calendar
import datetime
from decimal import Decimal
from typing import Any, Dict, List, Optional, Tuple

import swagger_client as saltedge_client
from budget.models import Account, Category, Connection, Transaction
from django.db.models import QuerySet, Sum
from users.models import User


def import_saltedge_connection(
    saltedge_connection: saltedge_client.Connection, user: User
) -> Tuple[Connection, bool]:
    return Connection.objects.update_or_create(
        external_id=int(saltedge_connection.id),
        defaults={"provider": saltedge_connection.provider_name, "user": user},
    )


def import_saltedge_connections(
    saltedge_connections: List[saltedge_client.Connection], user: User
) -> List[Tuple["Connection", bool]]:
    output = []
    for saltedge_connection in saltedge_connections:
        output.append(import_saltedge_connection(saltedge_connection, user))
    return output


def import_saltedge_accounts(
    saltedge_accounts: List[saltedge_client.Account], user: User
) -> List[Tuple["Account", bool]]:
    output = []
    for saltedge_account in saltedge_accounts:
        alias = (
            saltedge_account.extra.account_name
            if saltedge_account.extra.account_name
            else ""
        )
        o = Account.objects.update_or_create(
            external_id=int(saltedge_account.id),
            defaults={
                "name": saltedge_account.name,
                "alias": alias,
                "connection": Connection.objects.get(
                    external_id=int(saltedge_account.connection_id)
                ),
                "user": user,
            },
        )
        output.append(o)
    return output


def import_saltedge_transactions(
    saltedge_transactions: List[saltedge_client.Transaction], user: User
) -> List[Tuple["Transaction", bool]]:
    output = []
    for saltedge_transaction in saltedge_transactions:
        o = Transaction.objects.update_or_create(
            external_id=int(saltedge_transaction.id),
            defaults={
                "date": saltedge_transaction.made_on,
                "amount": saltedge_transaction.amount,
                "description": saltedge_transaction.description,
                "account": Account.objects.get(
                    external_id=saltedge_transaction.account_id
                ),
                "user": user,
            },
        )
        output.append(o)
    return output


def create_initial_balance(
    account: Account,
    saltedge_account: saltedge_client.Account,
    saltedge_transactions: List[saltedge_client.Transaction],
) -> Transaction:
    initial_balance = saltedge_account.balance - sum_saltedge_transactions(
        saltedge_transactions
    )
    oldest_saltedge_transaction = get_oldest_saltedge_transaction(saltedge_transactions)
    made_on = (
        oldest_saltedge_transaction.made_on
        if oldest_saltedge_transaction
        else datetime.date.today()
    )
    return Transaction.objects.create(
        date=made_on,
        amount=initial_balance,
        description="Initial balance",
        account=account,
        user=account.user,
    )


def sum_saltedge_transactions(transactions: List[saltedge_client.Transaction]) -> float:
    return sum(t.amount for t in transactions)


def get_oldest_saltedge_transaction(
    transactions: List[saltedge_client.Transaction],
) -> Optional[saltedge_client.Transaction]:
    oldest = None
    for transaction in transactions:
        if not oldest or transaction.made_on < oldest.made_on:
            oldest = transaction
    return oldest


def get_income_report(
    accounts: List[Account],
    from_date: datetime.date,
    to_date: datetime.date,
    excluded_categories: Optional[List[Category]] = None,
) -> Dict[str, Any]:
    income_records = get_income_record_per_month(
        accounts, from_date, to_date, excluded_categories
    )
    summary = get_income_records_summary(income_records)
    return {"income_records": income_records, "summary": summary}


def get_income_record_per_month(
    accounts: List[Account],
    from_date: datetime.date,
    to_date: datetime.date,
    excluded_categories: Optional[List[Category]] = None,
) -> List[Dict[str, Any]]:
    records = []
    for start, end in get_date_range_per_month(from_date, to_date):
        record = get_income_record(accounts, start, end, excluded_categories)
        records.append(record)
    return records


def get_date_range_per_month(
    from_date: datetime.date, to_date: datetime.date
) -> List[Tuple[datetime.date, datetime.date]]:
    date_ranges = []
    start_date = from_date
    while abs(diff_month(start_date, to_date)) > 0:
        end_date = get_month_end(start_date)
        date_ranges.append((start_date, end_date))
        start_date = get_month_start(add_month(start_date))
    date_ranges.append((start_date, to_date))
    return date_ranges


def diff_month(from_date: datetime.date, to_date: datetime.date) -> int:
    return (from_date.year - to_date.year) * 12 + from_date.month - to_date.month


def add_month(date: datetime.date) -> datetime.date:
    year = date.year + date.month // 12
    month = date.month % 12 + 1
    day = min(date.day, calendar.monthrange(year, month)[1])
    return datetime.date(year, month, day)


def get_month_start(date: datetime.date) -> datetime.date:
    return datetime.date(date.year, date.month, 1)


def get_month_end(date: datetime.date) -> datetime.date:
    return datetime.date(
        date.year, date.month, calendar.monthrange(date.year, date.month)[1]
    )


def get_income_record(
    accounts: List[Account],
    from_date: datetime.date,
    to_date: datetime.date,
    excluded_categories: Optional[List[Category]] = None,
) -> Dict[str, Any]:
    transactions = get_income_transactions(
        accounts, from_date, to_date, excluded_categories
    )
    revenue = get_revenue(transactions)
    expenses = get_expenses(transactions)
    income = revenue - expenses
    opening_balance = get_opening_balance(from_date, accounts)
    ending_balance = get_ending_balance(to_date, accounts)
    return {
        "from": from_date,
        "to": to_date,
        "revenue": revenue,
        "expenses": expenses,
        "income": income,
        "opening_balance": opening_balance,
        "ending_balance": ending_balance,
    }


def get_income_transactions(
    accounts: List[Account],
    from_date: datetime.date,
    to_date: datetime.date,
    excluded_categories: Optional[List[Category]] = None,
) -> QuerySet:
    filter_query: Dict[str, Any] = {
        "account__in": accounts,
    }
    filter_query["date__gte"] = from_date
    filter_query["date__lte"] = to_date
    transactions = Transaction.objects.filter(**filter_query)
    if excluded_categories:
        transactions = transactions.exclude(category__in=excluded_categories)
    return transactions


def get_revenue(transactions: QuerySet) -> Decimal:
    revenue_transactions = transactions.filter(amount__gt=0.0)
    revenue = revenue_transactions.aggregate(Sum("amount"))["amount__sum"]
    return revenue if revenue else Decimal()


def get_expenses(transactions: QuerySet) -> Decimal:
    expense_transactions = transactions.filter(amount__lt=0.0)
    expenses = expense_transactions.aggregate(Sum("amount"))["amount__sum"]
    return abs(expenses) if expenses else Decimal()


def get_opening_balance(date: datetime.date, accounts: List[Account]) -> Decimal:
    all_transactions = Transaction.objects.filter(account__in=accounts, date__lt=date)
    opening_balance = all_transactions.aggregate(Sum("amount"))["amount__sum"]
    return opening_balance if opening_balance else Decimal()


def get_ending_balance(date: datetime.date, accounts: List[Account]) -> Decimal:
    all_transactions = Transaction.objects.filter(account__in=accounts, date__lte=date)
    ending_balance = all_transactions.aggregate(Sum("amount"))["amount__sum"]
    return ending_balance if ending_balance else Decimal()


def get_income_records_summary(income_records: List[Dict[str, Any]]) -> Dict[str, Any]:
    revenue = Decimal()
    expenses = Decimal()
    income = Decimal()
    for b in income_records:
        revenue += b["revenue"]
        expenses += b["expenses"]
        income += b["income"]
    opening_balance = (
        income_records[0]["opening_balance"] if income_records else Decimal()
    )
    ending_balance = (
        income_records[-1]["ending_balance"] if income_records else Decimal()
    )
    return {
        "revenue": revenue,
        "expenses": expenses,
        "income": income,
        "opening_balance": opening_balance,
        "ending_balance": ending_balance,
    }
