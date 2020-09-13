import swagger_client as saltedge_client
import pytest
from pytest_mock import MockerFixture


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
            created_at="2020-09-07T10:35:46Z",
            id="888888888888888888",
            interactive_fields_names=None,
            interactive_html=None,
            name="finish",
            updated_at="2020-09-07T10:35:46Z",
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
        created_at="2020-09-07T11:35:46Z",
        custom_fields=None,
        device_type="desktop",
        remote_ip="93.184.216.34",
        exclude_accounts=None,
        user_present=False,
        customer_last_logged_at="2020-09-07T08:35:46Z",
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
        success_at="2020-09-07T11:35:46Z",
        to_date=None,
        updated_at="2020-09-07T11:35:46Z",
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
        created_at="2020-09-06T11:35:46Z",
        updated_at="2020-09-07T10:55:46Z",
        last_success_at="2020-09-07T10:55:46Z",
        status="active",
        country_code="XF",
        next_refresh_possible_at="2020-09-07T12:35:46Z",
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
