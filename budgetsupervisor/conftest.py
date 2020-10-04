import pytest
import datetime
import swagger_client as saltedge_client
import saltedge_wrapper.factory
import os
from budget.models import Category, Account, Connection, Transaction
from pytest_mock import MockerFixture
from django.utils.dateparse import parse_datetime, parse_date
from selenium.webdriver.firefox.webdriver import WebDriver


@pytest.fixture
@pytest.mark.django_db
def user_factory(django_user_model):
    def create_user(
        username,
        password="password",
        first_name="foo",
        last_name="bar",
        email="foo@example.com",
        is_staff=False,
        is_superuser=False,
        is_active=True,
    ):
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
def user_foo(user_factory):
    return user_factory(username="foo")


@pytest.fixture
@pytest.mark.django_db
def profile_factory(user_foo):
    def create_profile(
        user=user_foo, external_id=None,
    ):
        profile = user.profile
        profile.external_id = external_id
        profile.save()
        return profile

    return create_profile


@pytest.fixture
def profile_foo(profile_factory):
    return profile_factory()


@pytest.fixture
def profile_foo_external(profile_factory):
    return profile_factory(external_id=123)


@pytest.fixture
@pytest.mark.django_db
def login_user(client):
    def f(user, password="password"):
        client.login(username=user.username, password=password)

    return f


@pytest.fixture
@pytest.mark.django_db
def account_factory(connection_foo, user_foo):
    def create_account(
        name,
        account_type=Account.AccountType.ACCOUNT,
        external_id=None,
        connection=connection_foo,
        user=user_foo,
    ):
        return Account.objects.create(
            name=name,
            account_type=account_type,
            external_id=external_id,
            connection=connection,
            user=user,
        )

    return create_account


@pytest.fixture
def account_foo(account_factory):
    return account_factory("foo")


@pytest.fixture
def account_foo_external(account_factory, connection_foo_external):
    return account_factory("foo", external_id=123, connection=connection_foo_external)


@pytest.fixture
@pytest.mark.django_db
def category_factory(user_foo):
    def create_category(name, user=user_foo):
        return Category.objects.create(name=name, user=user)

    return create_category


@pytest.fixture
def category_foo(category_factory):
    return category_factory("foo")


@pytest.fixture
@pytest.mark.django_db
def connection_factory(user_foo):
    def create_connection(
        provider, user=user_foo, external_id=None,
    ):
        return Connection.objects.create(
            provider=provider, user=user, external_id=external_id
        )

    return create_connection


@pytest.fixture
def connection_foo(connection_factory):
    return connection_factory("foo")


@pytest.fixture
def connection_foo_external(connection_factory, profile_foo_external):
    return connection_factory(
        provider="foo", user=profile_foo_external.user, external_id=123
    )


@pytest.fixture
@pytest.mark.django_db
def transaction_factory(account_foo, category_foo, user_foo):
    def create_transaction(
        date=datetime.date.today(),
        amount=100.00,
        payee="",
        category=category_foo,
        description="",
        account=account_foo,
        external_id=None,
        user=user_foo,
    ):
        return Transaction.objects.create(
            date=date,
            amount=amount,
            payee=payee,
            category=category,
            description=description,
            account=account,
            external_id=None,
            user=user,
        )

    return create_transaction


@pytest.fixture
def transaction_foo(transaction_factory):
    return transaction_factory(description="transaction foo")


@pytest.fixture
def transaction_foo_external(transaction_factory):
    return transaction_factory(description="transaction foo", external_id=123)


@pytest.fixture
def customers_api(mocker: MockerFixture) -> saltedge_client.CustomersApi:
    return mocker.MagicMock(spec_set=saltedge_client.CustomersApi)


@pytest.fixture
def connect_sessions_api(mocker: MockerFixture) -> saltedge_client.ConnectSessionsApi:
    return mocker.MagicMock(spec_set=saltedge_client.ConnectSessionsApi)


@pytest.fixture
def connections_api(mocker: MockerFixture) -> saltedge_client.ConnectionsApi:
    return mocker.MagicMock(spec_set=saltedge_client.ConnectionsApi)


@pytest.fixture
def accounts_api(mocker: MockerFixture) -> saltedge_client.AccountsApi:
    return mocker.MagicMock(spec_set=saltedge_client.AccountsApi)


@pytest.fixture
def transactions_api(mocker: MockerFixture) -> saltedge_client.TransactionsApi:
    return mocker.MagicMock(spec_set=saltedge_client.TransactionsApi)


@pytest.fixture
def saltedge_customer_factory():
    def create_customer(
        id="222222222222222222",
        identifier="12rv1212f1efxchsdhbgv",
        secret="AtQX6Q8vRyMrPjUVtW7J_O1n06qYQ25bvUJ8CIC80-8",
    ):
        return saltedge_client.Customer(id=id, identifier=identifier, secret=secret)

    return create_customer


@pytest.fixture
def saltedge_customer(saltedge_customer_factory):
    return saltedge_customer_factory()


@pytest.fixture
def saltedge_stage_factory():
    def create_stage(
        created_at=None,
        id=None,
        interactive_fields_names=None,
        interactive_html=None,
        name=None,
        updated_at=None,
    ):
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
def saltedge_stage(saltedge_stage_factory):
    return saltedge_stage_factory(saltedge_stage_factory)


@pytest.fixture
def saltedge_simplified_attempt_factory(saltedge_stage):
    def create_simplified_attempt(
        api_mode="service",
        api_version="5",
        automatic_fetch=True,
        daily_refresh=False,
        categorization="personal",
        created_at=parse_datetime("2020-09-07T11:35:46Z"),
        custom_fields=None,
        device_type="desktop",
        remote_ip="93.184.216.34",
        exclude_accounts=None,
        user_present=False,
        customer_last_logged_at=parse_datetime("2020-09-07T08:35:46Z"),
        fail_at=None,
        fail_error_class=None,
        fail_message=None,
        fetch_scopes=None,
        finished=True,
        finished_recent=True,
        from_date=None,
        id="777777777777777777",
        interactive=False,
        locale="en",
        partial=False,
        store_credentials=True,
        success_at=parse_datetime("2020-09-07T11:35:46Z"),
        to_date=None,
        updated_at=parse_datetime("2020-09-07T11:35:46Z"),
        show_consent_confirmation=False,
        include_natures=None,
        last_stage=None,
    ):
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
def saltedge_simplified_attempt(saltedge_simplified_attempt_factory):
    return saltedge_simplified_attempt_factory()


@pytest.fixture
def saltedge_connection_factory(saltedge_simplified_attempt):
    def create_connection(
        id="111111111111111111",
        secret="AtQX6Q8vRyMrPjUVtW7J_O1n06qYQ25bvUJ8CIC80-8",
        provider_id="1234",
        provider_code="fakebank_simple_xf",
        provider_name="Fakebank Simple",
        daily_refresh=False,
        customer_id="222222222222222222",
        created_at=parse_datetime("2020-09-06T11:35:46Z"),
        updated_at=parse_datetime("2020-09-07T10:55:46Z"),
        last_success_at=parse_datetime("2020-09-07T10:55:46Z"),
        status="active",
        country_code="XF",
        next_refresh_possible_at=parse_datetime("2020-09-07T12:35:46Z"),
        store_credentials=True,
        last_attempt=None,
        show_consent_confirmation=False,
        last_consent_id="555555555555555555",
    ):
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
def saltedge_connection(saltedge_connection_factory):
    return saltedge_connection_factory()


@pytest.fixture
def saltedge_account_factory():
    def create_account(
        id="333333333333333333",
        name="Fake account 1",
        nature="card",
        balance=2007.2,
        currency_code="EUR",
        extra=None,
        connection_id="111111111111111111",
        created_at=parse_datetime("2020-09-07T08:35:46Z"),
        updated_at=parse_datetime("2020-09-07T08:35:46Z"),
    ):
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
def saltedge_account(saltedge_account_factory):
    return saltedge_account_factory()


@pytest.fixture
def saltedge_transaction_factory():
    def create_transaction(
        id="444444444444444444",
        mode="normal",
        status="posted",
        made_on=parse_date("2020-05-03"),
        amount=-200.0,
        currency_code="USD",
        description="test transaction",
        category="income",
        duplicated=False,
        extra=None,
        account_id="333333333333333333",
        created_at=parse_datetime("2020-09-05T11:35:46Z"),
        updated_at=parse_datetime("2020-09-06T11:35:46Z"),
    ):
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
def saltedge_transaction(saltedge_transaction_factory):
    return saltedge_transaction_factory()


@pytest.fixture(scope="class")
def selenium():
    s = WebDriver()
    yield s
    s.quit()


@pytest.fixture
def live_server_path(live_server):
    def f(path):
        return live_server.url + path

    return f


@pytest.fixture
def authenticate_selenium(selenium, live_server, client, user_foo):
    def f(
        user=user_foo,
        password="password",
        selenium=selenium,
        live_server=live_server,
        client=client,
    ):
        client.login(username=user.username, password=password)
        selenium.get(live_server.url)
        cookie = client.cookies["sessionid"]
        selenium.add_cookie(
            {"name": "sessionid", "value": cookie.value, "secure": False, "path": "/"}
        )
        return selenium

    return f


@pytest.fixture
def predefined_customer():
    return (
        saltedge_wrapper.factory.customers_api()
        .customers_customer_id_get(os.environ["CUSTOMER_ID"])
        .data
    )


@pytest.fixture
def predefined_saltedge_connection():
    return (
        saltedge_wrapper.factory.connections_api()
        .connections_connection_id_get(os.environ["CONNECTION_ID"])
        .data
    )


@pytest.fixture
def predefined_saltedge_account(predefined_saltedge_connection):
    return (
        saltedge_wrapper.factory.accounts_api()
        .accounts_get(predefined_saltedge_connection.id)
        .data[0]
    )


@pytest.fixture
def predefined_user(user_factory, predefined_customer):
    return user_factory(username=predefined_customer.identifier)


@pytest.fixture
def predefined_profile(profile_factory, predefined_customer, predefined_user):
    return profile_factory(user=predefined_user, external_id=predefined_customer.id)


@pytest.fixture
def predefined_connection(
    connection_factory, predefined_saltedge_connection, predefined_user
):
    return connection_factory(
        provider=predefined_saltedge_connection.provider_name,
        external_id=predefined_saltedge_connection.id,
        user=predefined_user,
    )


@pytest.fixture
def predefined_account(
    account_factory, predefined_saltedge_account, predefined_connection, predefined_user
):
    return account_factory(
        name=predefined_saltedge_account.name,
        external_id=predefined_saltedge_account.id,
        connection=predefined_connection,
        user=predefined_user,
    )
