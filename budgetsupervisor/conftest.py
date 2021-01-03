import datetime
import os
from typing import Callable, Dict, List, Tuple

import pytest
import saltedge_wrapper.factory
import swagger_client as saltedge_client
from budget.models import Account, Category, Connection, Transaction
from django.test import Client
from django.utils.dateparse import parse_date, parse_datetime
from pytest_django.live_server_helper import LiveServer
from pytest_mock import MockFixture
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import WebDriver
from users.models import Profile, User


@pytest.fixture
@pytest.mark.django_db
def user_factory(django_user_model: User) -> Callable[..., User]:
    def create_user(
        username: str,
        password: str = "password",
        first_name: str = "foo",
        last_name: str = "bar",
        email: str = "foo@example.com",
        is_staff: bool = False,
        is_superuser: bool = False,
        is_active: bool = True,
    ) -> User:
        return django_user_model.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
        )

    return create_user


@pytest.fixture
def user_foo(user_factory: Callable[..., User]) -> User:
    return user_factory(username="foo")


@pytest.fixture
def user_foo_inactive(user_factory: Callable[..., User]) -> User:
    return user_factory(username="foo", is_active=False)


@pytest.fixture
@pytest.mark.django_db
def profile_factory(user_foo: User) -> Callable[..., Profile]:
    def create_profile(user: User = user_foo, external_id: int = None) -> Profile:
        profile = user.profile
        profile.external_id = external_id
        profile.save()
        return profile

    return create_profile


@pytest.fixture
def profile_foo(profile_factory: Callable[..., Profile]) -> Profile:
    return profile_factory()


@pytest.fixture
def profile_foo_external(profile_factory: Callable[..., Profile]) -> Profile:
    return profile_factory(external_id=123)


@pytest.fixture
@pytest.mark.django_db
def login_user(client: Client) -> Callable[..., None]:
    def f(user: User, password: str = "password") -> None:
        client.login(username=user.username, password=password)

    return f


@pytest.fixture
@pytest.mark.django_db
def account_factory(user_foo: User) -> Callable[..., Account]:
    def create_account(
        name: str,
        alias: str = "",
        account_type: Tuple[str, str] = Account.AccountType.ACCOUNT,
        external_id: int = None,
        connection: Connection = None,
        user: User = user_foo,
    ) -> Account:
        return Account.objects.create(
            name=name,
            alias=alias,
            account_type=account_type,
            external_id=external_id,
            connection=connection,
            user=user,
        )

    return create_account


@pytest.fixture
def account_foo(account_factory: Callable[..., Account]) -> Account:
    return account_factory("foo")


@pytest.fixture
def account_foo_external(
    account_factory: Callable[..., Account], connection_foo: Connection
) -> Account:
    return account_factory("foo", external_id=123, connection=connection_foo)


@pytest.fixture
@pytest.mark.django_db
def category_factory(user_foo: User) -> Callable[..., Category]:
    def create_category(name: str, user: User = user_foo) -> Category:
        return Category.objects.create(name=name, user=user)

    return create_category


@pytest.fixture
def category_foo(category_factory: Callable[..., Category]) -> Category:
    return category_factory("foo")


@pytest.fixture
@pytest.mark.django_db
def connection_factory(user_foo: User) -> Callable[..., Connection]:
    def create_connection(
        provider: str, user: User = user_foo, external_id: int = 123,
    ) -> Connection:
        return Connection.objects.create(
            provider=provider, user=user, external_id=external_id
        )

    return create_connection


@pytest.fixture
def connection_foo(
    connection_factory: Callable[..., Connection], profile_foo_external: Profile
) -> Connection:
    return connection_factory(
        provider="foo", user=profile_foo_external.user, external_id=123
    )


@pytest.fixture
@pytest.mark.django_db
def transaction_factory(
    account_foo: Account, user_foo: User
) -> Callable[..., Transaction]:
    today = datetime.date.today()

    def create_transaction(
        date: datetime.date = today,
        amount: float = 100.00,
        payee: str = "",
        category: Category = None,
        description: str = "",
        account: Account = account_foo,
        external_id: int = None,
        user: User = user_foo,
    ) -> Transaction:
        return Transaction.objects.create(
            date=date,
            amount=amount,
            payee=payee,
            category=category,
            description=description,
            account=account,
            external_id=external_id,
            user=user,
        )

    return create_transaction


@pytest.fixture
def transaction_foo(transaction_factory: Callable[..., Transaction]) -> Transaction:
    return transaction_factory(description="transaction foo")


@pytest.fixture
def transaction_foo_external(
    transaction_factory: Callable[..., Transaction], account_foo_external: Account
) -> Transaction:
    return transaction_factory(
        description="transaction foo", external_id=123, account=account_foo_external
    )


@pytest.fixture
def customers_api(mocker: MockFixture) -> saltedge_client.CustomersApi:
    return mocker.MagicMock(spec_set=saltedge_client.CustomersApi)


@pytest.fixture
def connect_sessions_api(mocker: MockFixture) -> saltedge_client.ConnectSessionsApi:
    return mocker.MagicMock(spec_set=saltedge_client.ConnectSessionsApi)


@pytest.fixture
def connections_api(mocker: MockFixture) -> saltedge_client.ConnectionsApi:
    return mocker.MagicMock(spec_set=saltedge_client.ConnectionsApi)


@pytest.fixture
def accounts_api(mocker: MockFixture) -> saltedge_client.AccountsApi:
    return mocker.MagicMock(spec_set=saltedge_client.AccountsApi)


@pytest.fixture
def transactions_api(mocker: MockFixture) -> saltedge_client.TransactionsApi:
    return mocker.MagicMock(spec_set=saltedge_client.TransactionsApi)


@pytest.fixture
def saltedge_customer_factory() -> Callable[..., saltedge_client.Customer]:
    def create_customer(
        id: str = "222222222222222222",
        identifier: str = "12rv1212f1efxchsdhbgv",
        secret: str = "AtQX6Q8vRyMrPjUVtW7J_O1n06qYQ25bvUJ8CIC80-8",
    ) -> saltedge_client.Customer:
        return saltedge_client.Customer(id=id, identifier=identifier, secret=secret)

    return create_customer


@pytest.fixture
def saltedge_customer(
    saltedge_customer_factory: Callable[..., saltedge_client.Customer]
) -> saltedge_client.Customer:
    return saltedge_customer_factory()


@pytest.fixture
def saltedge_stage_factory() -> Callable[..., saltedge_client.Stage]:
    def create_stage(
        created_at: str = None,
        id: str = None,
        interactive_fields_names: str = None,
        interactive_html: str = None,
        name: str = None,
        updated_at: str = None,
    ) -> saltedge_client.Stage:
        return saltedge_client.Stage(
            created_at=parse_datetime("2020-09-07T10:35:46Z"),
            id="888888888888888888",
            interactive_fields_names=None,
            interactive_html=None,
            name="finish",
            updated_at=parse_datetime("2020-09-07T10:35:46Z"),
        )

    return create_stage


@pytest.fixture
def saltedge_stage(
    saltedge_stage_factory: Callable[..., saltedge_client.Stage]
) -> saltedge_client.Stage:
    return saltedge_stage_factory(saltedge_stage_factory)


@pytest.fixture
def saltedge_simplified_attempt_factory(
    saltedge_stage: saltedge_client.Stage,
) -> Callable[..., saltedge_client.SimplifiedAttempt]:
    created_at = parse_datetime("2020-09-07T11:35:46Z")
    customer_last_logged_at = parse_datetime("2020-09-07T08:35:46Z")
    success_at = parse_datetime("2020-09-07T11:35:46Z")
    updated_at = parse_datetime("2020-09-07T11:35:46Z")

    def create_simplified_attempt(
        api_mode: str = "service",
        api_version: str = "5",
        automatic_fetch: bool = True,
        daily_refresh: bool = False,
        categorization: str = "personal",
        created_at: str = created_at,
        custom_fields: Dict = None,
        device_type: str = "desktop",
        remote_ip: str = "93.184.216.34",
        exclude_accounts: List = None,
        user_present: bool = False,
        customer_last_logged_at: str = customer_last_logged_at,
        fail_at: str = None,
        fail_error_class: str = None,
        fail_message: str = None,
        fetch_scopes: List[str] = None,
        finished: bool = True,
        finished_recent: bool = True,
        from_date: str = None,
        id: str = "777777777777777777",
        interactive: bool = False,
        locale: str = "en",
        partial: bool = False,
        store_credentials: bool = True,
        success_at: str = success_at,
        to_date: str = None,
        updated_at: str = updated_at,
        show_consent_confirmation: bool = False,
        include_natures: List[str] = None,
        last_stage: str = None,
    ) -> saltedge_client.SimplifiedAttempt:
        if not custom_fields:
            custom_fields = {}
        if not exclude_accounts:
            exclude_accounts = []
        if not fetch_scopes:
            fetch_scopes = ["accounts", "transactions"]
        if not include_natures:
            include_natures = ["account", "card", "bonus"]
        if not last_stage:
            last_stage = saltedge_stage
        return saltedge_client.SimplifiedAttempt(
            api_mode=api_mode,
            api_version=api_version,
            automatic_fetch=automatic_fetch,
            daily_refresh=daily_refresh,
            categorization=categorization,
            created_at=created_at,
            custom_fields=custom_fields,
            device_type=device_type,
            remote_ip=remote_ip,
            exclude_accounts=exclude_accounts,
            user_present=user_present,
            customer_last_logged_at=customer_last_logged_at,
            fail_at=fail_at,
            fail_error_class=fail_error_class,
            fail_message=fail_message,
            fetch_scopes=fetch_scopes,
            finished=finished,
            finished_recent=finished_recent,
            from_date=from_date,
            id=id,
            interactive=interactive,
            locale=locale,
            partial=partial,
            store_credentials=store_credentials,
            success_at=success_at,
            to_date=to_date,
            updated_at=updated_at,
            show_consent_confirmation=show_consent_confirmation,
            include_natures=include_natures,
            last_stage=last_stage,
        )

    return create_simplified_attempt


@pytest.fixture
def saltedge_simplified_attempt(
    saltedge_simplified_attempt_factory: Callable[
        ..., saltedge_client.SimplifiedAttempt
    ]
) -> saltedge_client.SimplifiedAttempt:
    return saltedge_simplified_attempt_factory()


@pytest.fixture
def saltedge_connection_factory(
    saltedge_simplified_attempt: saltedge_client.SimplifiedAttempt,
) -> saltedge_client.Connection:
    created_at = parse_datetime("2020-09-06T11:35:46Z")
    updated_at = parse_datetime("2020-09-07T10:55:46Z")
    last_success_at = parse_datetime("2020-09-07T10:55:46Z")
    next_refresh_possible_at = parse_datetime("2020-09-07T12:35:46Z")

    def create_connection(
        id: str = "111111111111111111",
        secret: str = "AtQX6Q8vRyMrPjUVtW7J_O1n06qYQ25bvUJ8CIC80-8",
        provider_id: str = "1234",
        provider_code: str = "fakebank_simple_xf",
        provider_name: str = "Fakebank Simple",
        daily_refresh: bool = False,
        customer_id: str = "222222222222222222",
        created_at: str = created_at,
        updated_at: str = updated_at,
        last_success_at: str = last_success_at,
        status: str = "active",
        country_code: str = "XF",
        next_refresh_possible_at: str = next_refresh_possible_at,
        store_credentials: bool = True,
        last_attempt: saltedge_client.SimplifiedAttempt = None,
        show_consent_confirmation: bool = False,
        last_consent_id: str = "555555555555555555",
    ) -> saltedge_client.Connection:
        if not last_attempt:
            last_attempt = saltedge_simplified_attempt
        return saltedge_client.Connection(
            id=id,
            secret=secret,
            provider_id=provider_id,
            provider_code=provider_code,
            provider_name=provider_name,
            daily_refresh=daily_refresh,
            customer_id=customer_id,
            created_at=created_at,
            updated_at=updated_at,
            last_success_at=last_success_at,
            status=status,
            country_code=country_code,
            next_refresh_possible_at=next_refresh_possible_at,
            store_credentials=store_credentials,
            last_attempt=last_attempt,
            show_consent_confirmation=show_consent_confirmation,
            last_consent_id=last_consent_id,
        )

    return create_connection


@pytest.fixture
def saltedge_connection(
    saltedge_connection_factory: Callable[..., saltedge_client.Connection]
) -> saltedge_client.Connection:
    return saltedge_connection_factory()


@pytest.fixture
def saltedge_account_factory() -> saltedge_client.Account:
    created_at = parse_datetime("2020-09-07T08:35:46Z")
    updated_at = parse_datetime("2020-09-07T08:35:46Z")

    def create_account(
        id: str = "333333333333333333",
        name: str = "Fake account 1",
        nature: str = "card",
        balance: float = 2007.2,
        currency_code: str = "EUR",
        extra: Dict = None,
        connection_id: str = "111111111111111111",
        created_at: str = created_at,
        updated_at: str = updated_at,
    ) -> saltedge_client.Account:
        if not extra:
            extra = {"client_name": "Fake name"}
        return saltedge_client.Account(
            id=id,
            name=name,
            nature=nature,
            balance=balance,
            currency_code=currency_code,
            extra=extra,
            connection_id=connection_id,
            created_at=created_at,
            updated_at=updated_at,
        )

    return create_account


@pytest.fixture
def saltedge_account(
    saltedge_account_factory: Callable[..., saltedge_client.Account]
) -> saltedge_client.Account:
    return saltedge_account_factory()


@pytest.fixture
def saltedge_transaction_factory() -> Callable[..., saltedge_client.Transaction]:
    made_on = parse_date("2020-05-03")
    created_at = parse_datetime("2020-09-05T11:35:46Z")
    updated_at = parse_datetime("2020-09-06T11:35:46Z")

    def create_transaction(
        id: str = "444444444444444444",
        mode: str = "normal",
        status: str = "posted",
        made_on: datetime.date = made_on,
        amount: float = -200.0,
        currency_code: str = "USD",
        description: str = "test transaction",
        category: str = "income",
        duplicated: bool = False,
        extra: Dict = None,
        account_id: str = "333333333333333333",
        created_at: str = created_at,
        updated_at: str = updated_at,
    ) -> saltedge_client.Transaction:
        if not extra:
            extra = {
                "original_amount": -3974.6,
                "original_currency_code": "CZK",
                "posting_date": parse_date("2020-05-07"),
                "time": "23:56:12",
            }
        return saltedge_client.Transaction(
            id=id,
            mode=mode,
            status=status,
            made_on=made_on,
            amount=amount,
            currency_code=currency_code,
            description=description,
            category=category,
            duplicated=duplicated,
            extra=extra,
            account_id=account_id,
            created_at=created_at,
            updated_at=updated_at,
        )

    return create_transaction


@pytest.fixture
def saltedge_transaction(
    saltedge_transaction_factory: Callable[..., saltedge_client.Transaction]
) -> saltedge_client.Transaction:
    return saltedge_transaction_factory()


@pytest.fixture(scope="class")
def selenium() -> WebDriver:
    o = Options()
    o.headless = True
    s = WebDriver(options=o)
    yield s
    s.quit()


@pytest.fixture
def live_server_path(live_server: LiveServer) -> Callable[[str], str]:
    def f(path: str) -> str:
        return live_server.url + path

    return f


@pytest.fixture
def authenticate_selenium(
    selenium: WebDriver, live_server: LiveServer, client: Client, user_foo: User
) -> Callable[..., WebDriver]:
    def f(
        user: User = user_foo,
        password: str = "password",
        selenium: WebDriver = selenium,
        live_server: LiveServer = live_server,
        client: Client = client,
    ) -> WebDriver:
        client.login(username=user.username, password=password)
        selenium.get(live_server.url)
        cookie = client.cookies["sessionid"]
        selenium.add_cookie(
            {"name": "sessionid", "value": cookie.value, "secure": False, "path": "/"}
        )
        return selenium

    return f


@pytest.fixture
def predefined_customer() -> saltedge_client.Customer:
    return (
        saltedge_wrapper.factory.customers_api()
        .customers_customer_id_get(os.environ["SALTEDGE_CUSTOMER_ID"])
        .data
    )


@pytest.fixture
def predefined_saltedge_connection() -> saltedge_client.Connection:
    return (
        saltedge_wrapper.factory.connections_api()
        .connections_connection_id_get(os.environ["SALTEDGE_CONNECTION_ID"])
        .data
    )


@pytest.fixture
def predefined_saltedge_account(
    predefined_saltedge_connection: saltedge_client.Connection,
) -> saltedge_client.Account:
    return (
        saltedge_wrapper.factory.accounts_api()
        .accounts_get(predefined_saltedge_connection.id)
        .data[0]
    )


@pytest.fixture
def predefined_user(
    user_factory: Callable[..., User], predefined_customer: saltedge_client.Customer
) -> User:
    return user_factory(username=predefined_customer.identifier)


@pytest.fixture
def predefined_profile(
    profile_factory: Callable[..., Profile],
    predefined_customer: saltedge_client.Customer,
    predefined_user: User,
) -> Profile:
    return profile_factory(user=predefined_user, external_id=predefined_customer.id)


@pytest.fixture
def predefined_connection(
    connection_factory: Callable[..., Connection],
    predefined_saltedge_connection: saltedge_client.Connection,
    predefined_user: User,
) -> Connection:
    return connection_factory(
        provider=predefined_saltedge_connection.provider_name,
        external_id=predefined_saltedge_connection.id,
        user=predefined_user,
    )


@pytest.fixture
def predefined_account(
    account_factory: Callable[..., Account],
    predefined_saltedge_account: saltedge_client.Account,
    predefined_connection: saltedge_client.Connection,
    predefined_user: User,
) -> Account:
    return account_factory(
        name=predefined_saltedge_account.name,
        external_id=predefined_saltedge_account.id,
        connection=predefined_connection,
        user=predefined_user,
    )
