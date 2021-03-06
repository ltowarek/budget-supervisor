import datetime
import logging
from typing import Callable, Iterator, List, Optional, Tuple

import pytest
import swagger_client as saltedge_client
from budget.models import Account, Category, Connection, Transaction
from budget.services import import_saltedge_connections
from django.shortcuts import reverse
from django.utils.dateparse import parse_date
from saltedge_wrapper.factory import connections_api
from saltedge_wrapper.utils import get_connections, remove_connection_from_saltedge
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from swagger_client.rest import ApiException
from users.models import Profile, User

pytestmark = pytest.mark.selenium


logger = logging.getLogger(__name__)


class TestIndex:
    pass


class TestConnectionList:
    def test_menu(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        url = live_server_path(reverse("connections:connection_list"))
        selenium.get(url)

        elements = selenium.find_elements_by_xpath(
            '//div[contains(@class, "btn-toolbar")]/a'
        )
        assert len(elements) == 1
        assert elements[0].text == "Create"
        assert elements[0].get_attribute("href") == live_server_path(
            reverse("connections:connection_create")
        )

    def test_table_header(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        url = live_server_path(reverse("connections:connection_list"))
        selenium.get(url)

        elements = selenium.find_elements_by_xpath("//table/thead/tr/th")
        assert len(elements) == 2
        assert elements[0].text == "Provider"
        assert elements[1].text == "Actions"

    def test_table_body(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        connection_factory: Callable[..., Connection],
        user_foo: User,
    ) -> None:
        number_of_connections = 20
        for i in range(number_of_connections):
            connection_factory(f"provider {i}", user=user_foo)
        connections = Connection.objects.filter(user=user_foo).order_by("provider")
        assert len(connections) == number_of_connections

        selenium = authenticate_selenium(user=user_foo)
        url = live_server_path(reverse("connections:connection_list"))
        selenium.get(url)

        elements = selenium.find_elements_by_xpath("//table/tbody/tr")
        assert len(elements) == len(connections)
        for element, connection in zip(elements, connections):
            cells = element.find_elements_by_xpath(".//td")
            assert len(cells) == 2

            assert cells[0].text == connection.provider

            actions = cells[1].find_elements_by_xpath(".//a")
            assert actions[0].text == "Update"
            assert actions[0].get_attribute("href") == live_server_path(
                reverse("connections:connection_update", kwargs={"pk": connection.pk})
            )
            assert actions[1].text == "Delete"
            assert actions[1].get_attribute("href") == live_server_path(
                reverse("connections:connection_delete", kwargs={"pk": connection.pk})
            )
            assert actions[2].text == "Refresh"
            assert actions[2].get_attribute("href") == live_server_path(
                reverse("connections:connection_refresh", kwargs={"pk": connection.pk})
            )

    def test_pagination(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        url = live_server_path(reverse("connections:connection_list"))
        selenium.get(url)

        elements = selenium.find_elements_by_class_name("pagination")
        assert elements


@pytest.fixture
def remove_temporary_connections(
    predefined_saltedge_connection: saltedge_client.Connection,
    predefined_customer: saltedge_client.Customer,
) -> Iterator[None]:
    yield
    connections = get_connections(predefined_customer.id, connections_api())
    for connection in connections:
        if connection.id != predefined_saltedge_connection.id:
            remove_connection_from_saltedge(connection.id, connections_api())


class TestConnectionCreate:
    def test_saltedge_connect_session_creation(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        predefined_profile: Profile,
        remove_temporary_connections: Callable[..., None],
    ) -> None:
        selenium = authenticate_selenium(user=predefined_profile.user)
        self.create_saltedge_connection(selenium, live_server_path)
        assert selenium.current_url == live_server_path(
            reverse("connections:connection_list")
        )

    def test_saltedge_connect_session_creation_with_date_range(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        predefined_profile: Profile,
        remove_temporary_connections: Callable[..., None],
    ) -> None:
        selenium = authenticate_selenium(user=predefined_profile.user)
        self.create_saltedge_connection(
            selenium, live_server_path, datetime.date.today(), datetime.date.today()
        )
        assert selenium.current_url == live_server_path(
            reverse("connections:connection_list")
        )

    def test_cant_create_connection_if_external_synchronization_is_disabled(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        url = live_server_path(reverse("connections:connection_create"))
        selenium.get(url)
        element = selenium.find_element_by_id("synchronization")
        assert (
            element.text
            == "Enable external synchronization before creating a connection"
        )

    @classmethod
    def create_saltedge_connection(
        cls,
        selenium: WebDriver,
        live_server_path: Callable[[str], str],
        from_date: Optional[datetime.date] = None,
        to_date: Optional[datetime.date] = None,
    ) -> None:
        url = live_server_path(reverse("connections:connection_create"))
        selenium.get(url)
        if from_date:
            element = selenium.find_element_by_name("from_date")
            element.send_keys(from_date.isoformat())
        if to_date:
            element = selenium.find_element_by_name("to_date")
            element.send_keys(to_date.isoformat())
        element = selenium.find_element_by_xpath('//button[@type="submit"]')
        element.click()
        WebDriverWait(selenium, 20).until(
            EC.visibility_of_element_located((By.ID, "providers-search"))
        )
        element = selenium.find_element_by_id("providers-search")
        element.send_keys("Fake Demo Bank")
        element = selenium.find_element_by_class_name("tt-dropdown-menu")
        WebDriverWait(selenium, 20).until(EC.visibility_of(element))
        element = selenium.find_element_by_class_name("tt-suggestion")
        element.click()
        WebDriverWait(selenium, 20).until(
            EC.visibility_of_element_located((By.NAME, "username"))
        )
        element = selenium.find_element_by_name("username")
        element.send_keys("username")
        element = selenium.find_element_by_name("password")
        element.send_keys("secret")
        element = selenium.find_element_by_xpath('//input[@value="Proceed"]')
        element.click()
        element = selenium.find_element_by_xpath('//input[@value="Confirm"]')
        element.click()
        redirect_url = live_server_path(reverse("connections:connection_list"))
        WebDriverWait(selenium, 30).until(EC.url_to_be(redirect_url))


class TestConnectionUpdate:
    def test_dummy(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        connection_foo: Connection,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.update_connection(selenium, live_server_path, connection_foo)
        # There is no field to check
        assert True

    def test_message(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        connection_foo: Connection,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.update_connection(selenium, live_server_path, connection_foo)
        messages = [
            m.text
            for m in selenium.find_elements_by_xpath('//div[contains(@class, "alert")]')
        ]
        assert any(
            "Connection was updated successfully" in message for message in messages
        )

    def update_connection(
        self,
        selenium: WebDriver,
        live_server_path: Callable[[str], str],
        connection: Connection,
    ) -> None:
        url = live_server_path(
            reverse("connections:connection_update", kwargs={"pk": connection.pk})
        )
        selenium.get(url)
        element = selenium.find_element_by_xpath('//button[@type="submit"]')
        element.click()


@pytest.mark.skip(
    reason="next_refresh_possible_at prevents running multiple tests using the same saltedge connection"
)
class TestConnectionRefresh:
    def test_saltedge_connect_session_refresh(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        predefined_user: User,
        predefined_connection: Connection,
    ) -> None:
        selenium = authenticate_selenium(user=predefined_user)
        self.refresh_connection(selenium, live_server_path, predefined_connection)
        assert selenium.current_url == live_server_path(
            reverse("connections:connection_list")
        )

    def refresh_connection(
        self,
        selenium: WebDriver,
        live_server_path: Callable[[str], str],
        connection: Connection,
    ) -> None:
        url = live_server_path(
            reverse("connections:connection_refresh", kwargs={"pk": connection.pk})
        )
        selenium.get(url)
        element = selenium.find_element_by_xpath('//button[@type="submit"]')
        element.click()
        redirect_url = live_server_path(reverse("connections:connection_list"))
        WebDriverWait(selenium, 30).until(EC.url_to_be(redirect_url))


@pytest.fixture
def connection_external_factory(
    remove_temporary_connections: Callable[..., None],
    predefined_saltedge_connection: saltedge_client.Connection,
) -> Callable[..., Connection]:
    def f(
        selenium: WebDriver, live_server_path: Callable[[str], str], profile: Profile
    ) -> Connection:
        # There is no other way to create connection than using Selenium
        TestConnectionCreate.create_saltedge_connection(selenium, live_server_path)
        saltedge_connections = get_connections(profile.external_id, connections_api())
        connections = import_saltedge_connections(saltedge_connections, profile.user)
        return connections[1][0]

    return f


class TestConnectionDelete:
    def test_connection_is_deleted_internally(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        predefined_profile: Profile,
        connection_external_factory: Callable[..., Connection],
    ) -> None:
        selenium = authenticate_selenium(user=predefined_profile.user)
        connection = connection_external_factory(
            selenium, live_server_path, predefined_profile
        )
        self.delete_connection(selenium, live_server_path, connection)
        assert not Connection.objects.filter(pk=connection.pk).exists()

    def test_accounts_are_disconnected(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        predefined_profile: Profile,
        connection_external_factory: Callable[..., Connection],
        account_factory: Callable[..., Account],
    ) -> None:
        selenium = authenticate_selenium(user=predefined_profile.user)
        connection = connection_external_factory(
            selenium, live_server_path, predefined_profile
        )
        account = account_factory("foo", connection=connection, external_id=123)
        self.delete_connection(selenium, live_server_path, connection)
        account.refresh_from_db()
        assert account.external_id is None

    def test_transactions_are_disconnected(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        predefined_profile: Profile,
        connection_external_factory: Callable[..., Connection],
        account_factory: Callable[..., Account],
        transaction_factory: Callable[..., Account],
    ) -> None:
        selenium = authenticate_selenium(user=predefined_profile.user)
        connection = connection_external_factory(
            selenium, live_server_path, predefined_profile
        )
        account = account_factory("foo", connection=connection, external_id=123)
        transaction = transaction_factory(account=account, external_id=123)
        self.delete_connection(selenium, live_server_path, connection)
        transaction.refresh_from_db()
        assert transaction.external_id is None

    def test_connection_is_deleted_externally(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        predefined_profile: Profile,
        connection_external_factory: Callable[..., Connection],
    ) -> None:
        selenium = authenticate_selenium(user=predefined_profile.user)
        connection = connection_external_factory(
            selenium, live_server_path, predefined_profile
        )
        api = connections_api()
        assert api.connections_connection_id_get(connection.external_id)
        self.delete_connection(selenium, live_server_path, connection)
        with pytest.raises(ApiException) as e:
            api.connections_connection_id_get(connection.external_id)
        assert "ConnectionNotFound" in str(e.value)

    def test_redirect(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        predefined_profile: Profile,
        connection_external_factory: Callable[..., Connection],
    ) -> None:
        selenium = authenticate_selenium(user=predefined_profile.user)
        connection = connection_external_factory(
            selenium, live_server_path, predefined_profile
        )
        self.delete_connection(selenium, live_server_path, connection)
        assert selenium.current_url == live_server_path(
            reverse("connections:connection_list")
        )

    def test_message(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        predefined_profile: Profile,
        connection_external_factory: Callable[..., Connection],
    ) -> None:
        selenium = authenticate_selenium(user=predefined_profile.user)
        connection = connection_external_factory(
            selenium, live_server_path, predefined_profile
        )
        self.delete_connection(selenium, live_server_path, connection)
        messages = [
            m.text
            for m in selenium.find_elements_by_xpath('//div[contains(@class, "alert")]')
        ]
        assert any(
            "Connection was deleted successfully" in message for message in messages
        )

    def delete_connection(
        self,
        selenium: WebDriver,
        live_server_path: Callable[[str], str],
        connection: Connection,
    ) -> None:
        url = live_server_path(
            reverse("connections:connection_delete", kwargs={"pk": connection.pk})
        )
        selenium.get(url)
        element = selenium.find_element_by_xpath('//button[@type="submit"]')
        element.click()


class TestAccountList:
    def test_menu(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        url = live_server_path(reverse("accounts:account_list"))
        selenium.get(url)

        elements = selenium.find_elements_by_xpath(
            '//div[contains(@class, "btn-toolbar")]/a'
        )
        assert len(elements) == 1
        assert elements[0].text == "Create"
        assert elements[0].get_attribute("href") == live_server_path(
            reverse("accounts:account_create")
        )

    def test_table_header(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        url = live_server_path(reverse("accounts:account_list"))
        selenium.get(url)

        elements = selenium.find_elements_by_xpath("//table/thead/tr/th")
        assert len(elements) == 5
        assert elements[0].text == "Name"
        assert elements[1].text == "Alias"
        assert elements[2].text == "Type"
        assert elements[3].text == "Connection"
        assert elements[4].text == "Actions"

    def test_table_body(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        account_factory: Callable[..., Account],
        user_foo: User,
    ) -> None:
        number_of_accounts = 20
        for i in range(number_of_accounts):
            account_factory(
                name=f"account {i}",
                alias=f"alias {i}",
                account_type=Account.AccountType.ACCOUNT,
                external_id=None,
                connection=None,
                user=user_foo,
            )
            accounts = Account.objects.filter(user=user_foo).order_by("name")
        assert len(accounts) == number_of_accounts

        selenium = authenticate_selenium(user=user_foo)
        url = live_server_path(reverse("accounts:account_list"))
        selenium.get(url)

        elements = selenium.find_elements_by_xpath("//table/tbody/tr")
        assert len(elements) == len(accounts)
        for element, account in zip(elements, accounts):
            cells = element.find_elements_by_xpath(".//td")
            assert len(cells) == 5

            assert cells[0].text == account.name
            assert cells[1].text == account.alias
            assert cells[2].text == account.get_account_type_display()
            assert cells[3].text == str(account.connection)

            actions = cells[4].find_elements_by_xpath(".//a")
            assert actions[0].text == "Update"
            assert actions[0].get_attribute("href") == live_server_path(
                reverse("accounts:account_update", kwargs={"pk": account.pk})
            )
            assert actions[1].text == "Delete"
            assert actions[1].get_attribute("href") == live_server_path(
                reverse("accounts:account_delete", kwargs={"pk": account.pk})
            )

    def test_pagination(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        url = live_server_path(reverse("accounts:account_list"))
        selenium.get(url)

        elements = selenium.find_elements_by_class_name("pagination")
        assert elements

    def test_filtering(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        account_factory: Callable[..., Account],
        connection_foo: Connection,
    ) -> None:
        account_factory(
            name="foo",
            alias="foo_alias",
            account_type=Account.AccountType.ACCOUNT,
            connection=connection_foo,
            user=user_foo,
        )
        account_factory(
            name="bar",
            alias="bar_alias",
            account_type=Account.AccountType.CASH,
            connection=connection_foo,
            user=user_foo,
        )

        selenium = authenticate_selenium(user=user_foo)
        self.filter_accounts(
            selenium,
            live_server_path,
            name="foo",
            alias="foo_alias",
            account_types=[Account.AccountType.ACCOUNT],
            connections=[connection_foo],
        )

        elements = selenium.find_elements_by_xpath("//table/tbody/tr")
        assert len(elements) == 1

    def test_empty_filtering(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        account_factory: Callable[..., Account],
        connection_foo: Connection,
    ) -> None:
        account_factory(
            name="foo",
            alias="foo_alias",
            account_type=Account.AccountType.ACCOUNT,
            connection=connection_foo,
            user=user_foo,
        )
        account_factory(
            name="bar",
            alias="bar_alias",
            account_type=Account.AccountType.CASH,
            connection=connection_foo,
            user=user_foo,
        )

        selenium = authenticate_selenium(user=user_foo)
        self.filter_accounts(selenium, live_server_path)

        elements = selenium.find_elements_by_xpath("//table/tbody/tr")
        assert len(elements) == 2

    def filter_accounts(
        self,
        selenium: WebDriver,
        live_server_path: Callable[[str], str],
        name: Optional[str] = None,
        alias: Optional[str] = None,
        account_types: Optional[List[Tuple[str, str]]] = None,
        connections: Optional[List[Connection]] = None,
    ) -> None:
        url = live_server_path(reverse("accounts:account_list"))
        selenium.get(url)
        if name:
            element = selenium.find_element_by_name("name")
            element.send_keys(name)
        if alias:
            element = selenium.find_element_by_name("alias")
            element.send_keys(alias)
        if account_types:
            select = Select(selenium.find_element_by_name("account_types"))
            for t in account_types:
                select.select_by_visible_text(dict(Account.AccountType.choices)[t])
        if connections:
            select = Select(selenium.find_element_by_name("connections"))
            for c in connections:
                select.select_by_visible_text(str(c))
        element = selenium.find_element_by_xpath('//button[@type="submit"]')
        element.click()


class TestAccountCreate:
    def test_account_is_created(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.create_account(
            selenium, live_server_path, "account name", "account alias", "Cash"
        )
        account = Account.objects.filter(user=user_foo).last()
        assert account.name == "account name"
        assert account.alias == "account alias"
        assert account.account_type == Account.AccountType.CASH

    def test_redirect(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.create_account(
            selenium, live_server_path, "account name", "account alias", "Cash"
        )
        assert selenium.current_url == live_server_path(
            reverse("accounts:account_list")
        )

    def test_message(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.create_account(
            selenium, live_server_path, "account name", "account alias", "Cash"
        )
        messages = [
            m.text
            for m in selenium.find_elements_by_xpath('//div[contains(@class, "alert")]')
        ]
        assert any(
            "Account was created successfully" in message for message in messages
        )

    def create_account(
        self,
        selenium: WebDriver,
        live_server_path: Callable[[str], str],
        name: str,
        alias: str,
        account_type: str,
    ) -> None:
        url = live_server_path(reverse("accounts:account_create"))
        selenium.get(url)
        element = selenium.find_element_by_name("name")
        element.send_keys(name)
        element = selenium.find_element_by_name("alias")
        element.send_keys(alias)
        select = Select(selenium.find_element_by_name("account_type"))
        select.select_by_visible_text(account_type)
        element = selenium.find_element_by_xpath('//button[@type="submit"]')
        element.click()


class TestAccountUpdate:
    def test_account_is_updated(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        account_foo: Account,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.update_account(
            selenium,
            live_server_path,
            account_foo,
            "account name",
            "account alias",
            "Cash",
        )
        assert account_foo.name == "account name"
        assert account_foo.alias == "account alias"
        assert account_foo.account_type == Account.AccountType.CASH

    def test_redirect(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        account_foo: Account,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.update_account(
            selenium,
            live_server_path,
            account_foo,
            "account name",
            "account alias",
            "Cash",
        )
        assert selenium.current_url == live_server_path(
            reverse("accounts:account_list")
        )

    def test_message(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        account_foo: Account,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.update_account(
            selenium,
            live_server_path,
            account_foo,
            "account name",
            "account alias",
            "Cash",
        )
        messages = [
            m.text
            for m in selenium.find_elements_by_xpath('//div[contains(@class, "alert")]')
        ]
        assert any(
            "Account was updated successfully" in message for message in messages
        )

    def update_account(
        self,
        selenium: WebDriver,
        live_server_path: Callable[[str], str],
        account: Account,
        name: str,
        alias: str,
        account_type: str,
    ) -> None:
        url = live_server_path(
            reverse("accounts:account_update", kwargs={"pk": account.pk})
        )
        selenium.get(url)
        element = selenium.find_element_by_name("name")
        element.clear()
        element.send_keys(name)
        element = selenium.find_element_by_name("alias")
        element.clear()
        element.send_keys(alias)
        select = Select(selenium.find_element_by_name("account_type"))
        select.select_by_visible_text(account_type)
        element = selenium.find_element_by_xpath('//button[@type="submit"]')
        element.click()
        account.refresh_from_db()


class TestAccountDelete:
    def test_account_is_deleted(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        account_foo: Account,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.delete_account(selenium, live_server_path, account_foo)
        assert Account.objects.filter(user=user_foo).count() == 0

    def test_related_transactions_are_deleted(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        account_foo: Account,
        transaction_factory: Callable[..., Transaction],
    ) -> None:
        number_of_transactions = 20
        for _ in range(number_of_transactions):
            transaction_factory()
        selenium = authenticate_selenium(user=user_foo)
        self.delete_account(selenium, live_server_path, account_foo)
        assert Transaction.objects.filter(user=user_foo).count() == 0

    def test_redirect(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        account_foo: Account,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.delete_account(selenium, live_server_path, account_foo)
        assert selenium.current_url == live_server_path(
            reverse("accounts:account_list")
        )

    def test_message(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        account_foo: Account,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.delete_account(selenium, live_server_path, account_foo)
        messages = [
            m.text
            for m in selenium.find_elements_by_xpath('//div[contains(@class, "alert")]')
        ]
        assert any(
            "Account was deleted successfully" in message for message in messages
        )

    def delete_account(
        self,
        selenium: WebDriver,
        live_server_path: Callable[[str], str],
        account: Account,
    ) -> None:
        url = live_server_path(
            reverse("accounts:account_delete", kwargs={"pk": account.pk})
        )
        selenium.get(url)
        element = selenium.find_element_by_xpath('//button[@type="submit"]')
        element.click()


class TestTransactionList:
    def test_menu(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        url = live_server_path(reverse("transactions:transaction_list"))
        selenium.get(url)

        elements = selenium.find_elements_by_xpath(
            '//div[contains(@class, "btn-toolbar")]/a'
        )
        assert len(elements) == 1
        assert elements[0].text == "Create"
        assert elements[0].get_attribute("href") == live_server_path(
            reverse("transactions:transaction_create")
        )

    def test_table_header(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        url = live_server_path(reverse("transactions:transaction_list"))
        selenium.get(url)

        elements = selenium.find_elements_by_xpath("//table/thead/tr/th")
        assert len(elements) == 7
        assert elements[0].text == "Date"
        assert elements[1].text == "Amount"
        assert elements[2].text == "Payee"
        assert elements[3].text == "Category"
        assert elements[4].text == "Description"
        assert elements[5].text == "Account"
        assert elements[6].text == "Actions"

    def test_table_body(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        transaction_factory: Callable[..., Transaction],
        user_foo: User,
        category_foo: Category,
        account_foo: Account,
    ) -> None:
        number_of_transactions = 20
        for i in range(number_of_transactions):
            transaction_factory(
                date=datetime.date.today() - datetime.timedelta(days=i),
                amount=float(i),
                payee=f"payee {i}",
                category=category_foo,
                description=f"description {i}",
                account=account_foo,
                external_id=None,
                user=user_foo,
            )
            transactions = Transaction.objects.filter(user=user_foo).order_by("-date")
        assert len(transactions) == number_of_transactions

        selenium = authenticate_selenium(user=user_foo)
        url = live_server_path(reverse("transactions:transaction_list"))
        selenium.get(url)

        elements = selenium.find_elements_by_xpath("//table/tbody/tr")
        assert len(elements) == len(transactions)
        for element, transaction in zip(elements, transactions):
            cells = element.find_elements_by_xpath(".//td")
            assert len(cells) == 7

            # parse_date does not support SHORT_DATE_FORMAT
            assert parse_date(cells[0].text) is None
            assert cells[1].text == str(transaction.amount)
            assert cells[2].text == transaction.payee
            assert cells[3].text == str(transaction.category)
            assert cells[4].text == transaction.description
            assert cells[5].text == str(transaction.account)

            actions = cells[6].find_elements_by_xpath(".//a")
            assert actions[0].text == "Update"
            assert actions[0].get_attribute("href") == live_server_path(
                reverse(
                    "transactions:transaction_update", kwargs={"pk": transaction.pk}
                )
            )
            assert actions[1].text == "Delete"
            assert actions[1].get_attribute("href") == live_server_path(
                reverse(
                    "transactions:transaction_delete", kwargs={"pk": transaction.pk}
                )
            )

    def test_pagination(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        url = live_server_path(reverse("transactions:transaction_list"))
        selenium.get(url)

        elements = selenium.find_elements_by_class_name("pagination")
        assert elements

    def test_filtering(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        transaction_factory: Callable[..., Transaction],
        category_foo: Category,
        account_foo: Account,
    ) -> None:
        transaction_factory(
            date=datetime.date.today(),
            amount=150.0,
            category=category_foo,
            description="foo",
            account=account_foo,
            user=user_foo,
        )
        transaction_factory(
            date=datetime.date.today(),
            amount=50.0,
            category=category_foo,
            description="bar",
            account=account_foo,
            user=user_foo,
        )

        selenium = authenticate_selenium(user=user_foo)
        self.filter_transactions(
            selenium,
            live_server_path,
            from_date=datetime.date.today(),
            to_date=datetime.date.today(),
            min_amount=100.0,
            max_amount=200.0,
            categories=[category_foo],
            description="foo",
            accounts=[account_foo],
        )

        elements = selenium.find_elements_by_xpath("//table/tbody/tr")
        assert len(elements) == 1

    def test_empty_filtering(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        transaction_factory: Callable[..., Transaction],
        category_foo: Category,
        account_foo: Account,
    ) -> None:
        transaction_factory(
            date=datetime.date.today(),
            amount=150.0,
            category=category_foo,
            description="foo",
            account=account_foo,
            user=user_foo,
        )
        transaction_factory(
            date=datetime.date.today(),
            amount=50.0,
            category=category_foo,
            description="bar",
            account=account_foo,
            user=user_foo,
        )

        selenium = authenticate_selenium(user=user_foo)
        self.filter_transactions(selenium, live_server_path)

        elements = selenium.find_elements_by_xpath("//table/tbody/tr")
        assert len(elements) == 2

    def filter_transactions(
        self,
        selenium: WebDriver,
        live_server_path: Callable[[str], str],
        from_date: Optional[datetime.date] = None,
        to_date: Optional[datetime.date] = None,
        min_amount: Optional[float] = None,
        max_amount: Optional[float] = None,
        categories: Optional[List[Category]] = None,
        description: Optional[str] = None,
        accounts: Optional[List[Account]] = None,
    ) -> None:
        url = live_server_path(reverse("transactions:transaction_list"))
        selenium.get(url)
        if from_date:
            element = selenium.find_element_by_name("from_date")
            element.send_keys(from_date.strftime("%Y-%m-%d"))
        if to_date:
            element = selenium.find_element_by_name("to_date")
            element.send_keys(to_date.strftime("%Y-%m-%d"))
        if min_amount:
            element = selenium.find_element_by_name("min_amount")
            element.send_keys(str(min_amount))
        if max_amount:
            element = selenium.find_element_by_name("max_amount")
            element.send_keys(str(max_amount))
        if categories:
            select = Select(selenium.find_element_by_name("categories"))
            for c in categories:
                select.select_by_visible_text(str(c))
        if description:
            element = selenium.find_element_by_name("description")
            element.send_keys(description)
        if accounts:
            select = Select(selenium.find_element_by_name("accounts"))
            for a in accounts:
                select.select_by_visible_text(str(a))
        element = selenium.find_element_by_xpath('//button[@type="submit"]')
        element.click()


class TestTransactionCreate:
    def test_transaction_is_created(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        category_foo: Category,
        account_foo: Account,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.create_transaction(
            selenium,
            live_server_path,
            datetime.date.today(),
            100.0,
            "payee",
            category_foo,
            "description",
            account_foo,
        )
        transaction = Transaction.objects.filter(user=user_foo).last()
        assert transaction.date == datetime.date.today()
        assert transaction.amount == 100.0
        assert transaction.payee == "payee"
        assert transaction.category == category_foo
        assert transaction.description == "description"
        assert transaction.account == account_foo

    def test_transaction_category_can_be_empty(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        account_foo: Account,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.create_transaction(
            selenium,
            live_server_path,
            datetime.date.today(),
            100.0,
            "payee",
            None,
            "description",
            account_foo,
        )
        transaction = Transaction.objects.filter(user=user_foo).last()
        assert transaction.category is None

    def test_redirect(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        category_foo: Category,
        account_foo: Account,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.create_transaction(
            selenium,
            live_server_path,
            datetime.date.today(),
            100.0,
            "payee",
            category_foo,
            "description",
            account_foo,
        )
        assert selenium.current_url == live_server_path(
            reverse("transactions:transaction_list")
        )

    def test_message(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        category_foo: Category,
        account_foo: Account,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.create_transaction(
            selenium,
            live_server_path,
            datetime.date.today(),
            100.0,
            "payee",
            category_foo,
            "description",
            account_foo,
        )
        messages = [
            m.text
            for m in selenium.find_elements_by_xpath('//div[contains(@class, "alert")]')
        ]
        assert any(
            "Transaction was created successfully" in message for message in messages
        )

    def create_transaction(
        self,
        selenium: WebDriver,
        live_server_path: Callable[[str], str],
        date: datetime.date,
        amount: float,
        payee: str,
        category: Optional[Category],
        description: str,
        account: Account,
    ) -> None:
        url = live_server_path(reverse("transactions:transaction_create"))
        selenium.get(url)
        element = selenium.find_element_by_name("date")
        element.send_keys(date.isoformat())
        element = selenium.find_element_by_name("amount")
        element.send_keys(str(amount))
        element = selenium.find_element_by_name("payee")
        element.send_keys(payee)
        if category:
            select = Select(selenium.find_element_by_name("category"))
            select.select_by_visible_text(category.name)
        element = selenium.find_element_by_name("description")
        element.send_keys(description)
        select = Select(selenium.find_element_by_name("account"))
        select.select_by_visible_text(account.name)
        element = selenium.find_element_by_xpath('//button[@type="submit"]')
        element.click()


class TestTransactionUpdate:
    def test_transaction_is_updated(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        transaction_foo: Transaction,
        category_foo: Category,
        account_foo: Account,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.update_transaction(
            selenium,
            live_server_path,
            transaction_foo,
            datetime.date.today(),
            100.0,
            "payee",
            category_foo,
            "description",
            account_foo,
        )
        assert transaction_foo.date == datetime.date.today()
        assert transaction_foo.amount == 100.0
        assert transaction_foo.payee == "payee"
        assert transaction_foo.category == category_foo
        assert transaction_foo.description == "description"
        assert transaction_foo.account == account_foo

    def test_redirect(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        transaction_foo: Transaction,
        category_foo: Category,
        account_foo: Account,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.update_transaction(
            selenium,
            live_server_path,
            transaction_foo,
            datetime.date.today(),
            100.0,
            "payee",
            category_foo,
            "description",
            account_foo,
        )
        assert selenium.current_url == live_server_path(
            reverse("transactions:transaction_list")
        )

    def test_message(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        transaction_foo: Transaction,
        category_foo: Category,
        account_foo: Account,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.update_transaction(
            selenium,
            live_server_path,
            transaction_foo,
            datetime.date.today(),
            100.0,
            "payee",
            category_foo,
            "description",
            account_foo,
        )
        messages = [
            m.text
            for m in selenium.find_elements_by_xpath('//div[contains(@class, "alert")]')
        ]
        assert any(
            "Transaction was updated successfully" in message for message in messages
        )

    def update_transaction(
        self,
        selenium: WebDriver,
        live_server_path: Callable[[str], str],
        transaction: Transaction,
        date: datetime.date,
        amount: float,
        payee: str,
        category: Category,
        description: str,
        account: Account,
    ) -> None:
        url = live_server_path(
            reverse("transactions:transaction_update", kwargs={"pk": transaction.pk})
        )
        selenium.get(url)
        element = selenium.find_element_by_name("date")
        element.clear()
        element.send_keys(date.isoformat())
        element = selenium.find_element_by_name("amount")
        element.clear()
        element.send_keys(str(amount))
        element = selenium.find_element_by_name("payee")
        element.clear()
        element.send_keys(payee)
        select = Select(selenium.find_element_by_name("category"))
        select.select_by_visible_text(category.name)
        element = selenium.find_element_by_name("description")
        element.clear()
        element.send_keys(description)
        select = Select(selenium.find_element_by_name("account"))
        select.select_by_visible_text(account.name)
        element = selenium.find_element_by_xpath('//button[@type="submit"]')
        element.click()
        transaction.refresh_from_db()


class TestTransactionDelete:
    def test_transaction_is_deleted(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        transaction_foo: Transaction,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.delete_transaction(selenium, live_server_path, transaction_foo)
        assert Transaction.objects.filter(user=user_foo).count() == 0

    def test_redirect(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        transaction_foo: Transaction,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.delete_transaction(selenium, live_server_path, transaction_foo)
        assert selenium.current_url == live_server_path(
            reverse("transactions:transaction_list")
        )

    def test_message(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        transaction_foo: Transaction,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.delete_transaction(selenium, live_server_path, transaction_foo)
        messages = [
            m.text
            for m in selenium.find_elements_by_xpath('//div[contains(@class, "alert")]')
        ]
        assert any(
            "Transaction was deleted successfully" in message for message in messages
        )

    def delete_transaction(
        self,
        selenium: WebDriver,
        live_server_path: Callable[[str], str],
        transaction: Transaction,
    ) -> None:
        url = live_server_path(
            reverse("transactions:transaction_delete", kwargs={"pk": transaction.pk})
        )
        selenium.get(url)
        element = selenium.find_element_by_xpath('//button[@type="submit"]')
        element.click()


class TestCategoryList:
    def test_menu(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        url = live_server_path(reverse("categories:category_list"))
        selenium.get(url)

        elements = selenium.find_elements_by_xpath(
            '//div[contains(@class, "btn-toolbar")]/a'
        )
        assert len(elements) == 1
        assert elements[0].text == "Create"
        assert elements[0].get_attribute("href") == live_server_path(
            reverse("categories:category_create")
        )

    def test_table_header(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        url = live_server_path(reverse("categories:category_list"))
        selenium.get(url)

        elements = selenium.find_elements_by_xpath("//table/thead/tr/th")
        assert len(elements) == 2
        assert elements[0].text == "Name"
        assert elements[1].text == "Actions"

    def test_table_body(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        category_factory: Callable[..., Category],
        user_foo: User,
    ) -> None:
        existing_categories = Category.objects.filter(user=user_foo).count()
        number_of_categories = 5
        for i in range(number_of_categories):
            category_factory(
                name=f"category {i}", user=user_foo,
            )
        categories = Category.objects.filter(user=user_foo).order_by("name")
        assert len(categories) == number_of_categories + existing_categories

        selenium = authenticate_selenium(user=user_foo)
        url = live_server_path(reverse("categories:category_list"))
        selenium.get(url)

        elements = selenium.find_elements_by_xpath("//table/tbody/tr")
        assert len(elements) == len(categories)
        for element, category in zip(elements, categories):
            cells = element.find_elements_by_xpath(".//td")
            assert len(cells) == 2

            assert cells[0].text == category.name

            actions = cells[1].find_elements_by_xpath(".//a")
            assert actions[0].text == "Update"
            assert actions[0].get_attribute("href") == live_server_path(
                reverse("categories:category_update", kwargs={"pk": category.pk})
            )
            assert actions[1].text == "Delete"
            assert actions[1].get_attribute("href") == live_server_path(
                reverse("categories:category_delete", kwargs={"pk": category.pk})
            )

    def test_pagination(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        url = live_server_path(reverse("categories:category_list"))
        selenium.get(url)

        elements = selenium.find_elements_by_class_name("pagination")
        assert elements


class TestCategoryCreate:
    def test_category_is_created(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.create_category(selenium, live_server_path, "category foo")
        category = Category.objects.filter(user=user_foo).last()
        assert category.name == "category foo"

    def test_redirect(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.create_category(selenium, live_server_path, "category foo")
        assert selenium.current_url == live_server_path(
            reverse("categories:category_list")
        )

    def test_message(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.create_category(selenium, live_server_path, "category foo")
        messages = [
            m.text
            for m in selenium.find_elements_by_xpath('//div[contains(@class, "alert")]')
        ]
        assert any(
            "Category was created successfully" in message for message in messages
        )

    def create_category(
        self, selenium: WebDriver, live_server_path: Callable[[str], str], name: str
    ) -> None:
        url = live_server_path(reverse("categories:category_create"))
        selenium.get(url)
        element = selenium.find_element_by_name("name")
        element.send_keys(name)
        element = selenium.find_element_by_xpath('//button[@type="submit"]')
        element.click()


class TestCategoryUpdate:
    def test_category_is_updated(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        category_foo: Category,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.update_category(selenium, live_server_path, category_foo, "new name")
        assert category_foo.name == "new name"

    def test_redirect(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        category_foo: Category,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.update_category(selenium, live_server_path, category_foo, "new name")
        assert selenium.current_url == live_server_path(
            reverse("categories:category_list")
        )

    def test_message(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        category_foo: Category,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.update_category(selenium, live_server_path, category_foo, "new name")
        messages = [
            m.text
            for m in selenium.find_elements_by_xpath('//div[contains(@class, "alert")]')
        ]
        assert any(
            "Category was updated successfully" in message for message in messages
        )

    def update_category(
        self,
        selenium: WebDriver,
        live_server_path: Callable[[str], str],
        category: Category,
        name: str,
    ) -> None:
        url = live_server_path(
            reverse("categories:category_update", kwargs={"pk": category.pk})
        )
        selenium.get(url)
        element = selenium.find_element_by_name("name")
        element.clear()
        element.send_keys(name)
        element = selenium.find_element_by_xpath('//button[@type="submit"]')
        element.click()
        category.refresh_from_db()


class TestCategoryDelete:
    def test_category_is_deleted(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        category_foo: Category,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        existing_categories = Category.objects.filter(user=user_foo).count()
        self.delete_category(selenium, live_server_path, category_foo)
        assert Category.objects.filter(user=user_foo).count() == existing_categories - 1

    def test_redirect(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        category_foo: Category,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.delete_category(selenium, live_server_path, category_foo)
        assert selenium.current_url == live_server_path(
            reverse("categories:category_list")
        )

    def test_message(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        category_foo: Category,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.delete_category(selenium, live_server_path, category_foo)
        messages = [
            m.text
            for m in selenium.find_elements_by_xpath('//div[contains(@class, "alert")]')
        ]
        assert any(
            "Category was deleted successfully" in message for message in messages
        )

    def delete_category(
        self,
        selenium: WebDriver,
        live_server_path: Callable[[str], str],
        category: Category,
    ) -> None:
        url = live_server_path(
            reverse("categories:category_delete", kwargs={"pk": category.pk})
        )
        selenium.get(url)
        element = selenium.find_element_by_xpath('//button[@type="submit"]')
        element.click()


class TestReportIncome:
    def test_table_header(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        account_foo: Account,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.report_income(selenium, live_server_path, [account_foo])

        elements = selenium.find_elements_by_xpath("//table/thead/tr/th")
        expected = ["From", "To", "Revenue", "Expenses", "Income"]
        assert len(elements) == len(expected)
        for el, ex in zip(elements, expected):
            assert el.text == ex

    def test_table_body(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        account_foo: Account,
        category_foo: Category,
        transaction_factory: Callable[..., Transaction],
    ) -> None:
        months = 2
        from_date = datetime.date(2020, 1, 10)
        to_date = datetime.date(2020, 1 + months, 15)
        transaction_factory(date=from_date)

        selenium = authenticate_selenium(user=user_foo)
        self.report_income(
            selenium,
            live_server_path,
            [account_foo],
            from_date,
            to_date,
            [category_foo],
        )

        elements = selenium.find_elements_by_xpath("//table/tbody/tr/td")
        columns = 5
        assert len(elements) == (1 + months) * columns

    def test_table_footer(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        account_foo: Account,
        transaction_foo: Transaction,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.report_income(selenium, live_server_path, [account_foo])

        elements = selenium.find_elements_by_xpath("//table/tfoot/tr/th")
        columns = 5
        assert len(elements) == columns

    def report_income(
        self,
        selenium: WebDriver,
        live_server_path: Callable[[str], str],
        accounts: List[Account],
        from_date: Optional[datetime.date] = None,
        to_date: Optional[datetime.date] = None,
        excluded_categories: Optional[List[Category]] = None,
    ) -> None:
        if from_date is None:
            from_date = datetime.date.today()
        if to_date is None:
            to_date = datetime.date.today()
        url = live_server_path(reverse("reports:report_income"))
        selenium.get(url)
        select = Select(selenium.find_element_by_name("accounts"))
        for account in accounts:
            select.select_by_visible_text(account.name)
        element = selenium.find_element_by_name("from_date")
        element.send_keys(from_date.isoformat())
        element = selenium.find_element_by_name("to_date")
        element.send_keys(to_date.isoformat())
        if excluded_categories:
            select = Select(selenium.find_element_by_name("excluded_categories"))
            for c in excluded_categories:
                select.select_by_visible_text(c.name)
        element = selenium.find_element_by_xpath('//button[@type="submit"]')
        element.click()


class TestReportBalance:
    def test_table_header(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        account_foo: Account,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.report_balance(selenium, live_server_path, [account_foo])

        elements = selenium.find_elements_by_xpath("//table/thead/tr/th")
        expected = ["From", "To", "Opening balance", "Ending balance", "Difference"]
        assert len(elements) == len(expected)
        for el, ex in zip(elements, expected):
            assert el.text == ex

    def test_table_body(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        account_foo: Account,
        transaction_factory: Callable[..., Transaction],
    ) -> None:
        months = 2
        from_date = datetime.date(2020, 1, 10)
        to_date = datetime.date(2020, 1 + months, 15)
        transaction_factory(date=from_date)

        selenium = authenticate_selenium(user=user_foo)
        self.report_balance(
            selenium, live_server_path, [account_foo], from_date, to_date,
        )

        elements = selenium.find_elements_by_xpath("//table/tbody/tr/td")
        columns = 5
        assert len(elements) == (1 + months) * columns

    def test_table_footer(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        account_foo: Account,
        transaction_foo: Transaction,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.report_balance(selenium, live_server_path, [account_foo])

        elements = selenium.find_elements_by_xpath("//table/tfoot/tr/th")
        columns = 5
        assert len(elements) == columns

    def report_balance(
        self,
        selenium: WebDriver,
        live_server_path: Callable[[str], str],
        accounts: List[Account],
        from_date: Optional[datetime.date] = None,
        to_date: Optional[datetime.date] = None,
    ) -> None:
        if from_date is None:
            from_date = datetime.date.today()
        if to_date is None:
            to_date = datetime.date.today()
        url = live_server_path(reverse("reports:report_balance"))
        selenium.get(url)
        select = Select(selenium.find_element_by_name("accounts"))
        for account in accounts:
            select.select_by_visible_text(account.name)
        element = selenium.find_element_by_name("from_date")
        element.send_keys(from_date.isoformat())
        element = selenium.find_element_by_name("to_date")
        element.send_keys(to_date.isoformat())
        element = selenium.find_element_by_xpath('//button[@type="submit"]')
        element.click()


class TestReportCategoryBalance:
    def test_table_header(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        category_factory: Callable[..., Category],
        account_foo: Account,
    ) -> None:
        categories = [
            category_factory(name="category_a"),
            category_factory(name="category_b"),
        ]
        selenium = authenticate_selenium(user=user_foo)
        self.report_category_balance(
            selenium, live_server_path, categories, [account_foo]
        )

        elements = selenium.find_elements_by_xpath("//table/thead/tr/th")
        expected = ["From", "To", "category_a", "category_b"]
        assert len(elements) == len(expected)
        for el, ex in zip(elements, expected):
            assert el.text == ex

    def test_table_body(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        category_factory: Callable[..., Category],
        account_foo: Account,
        transaction_factory: Callable[..., Transaction],
    ) -> None:
        categories = [
            category_factory(name="category_a"),
            category_factory(name="category_b"),
        ]
        months = 2
        from_date = datetime.date(2020, 1, 10)
        to_date = datetime.date(2020, 1 + months, 15)
        transaction_factory(date=from_date)

        selenium = authenticate_selenium(user=user_foo)
        self.report_category_balance(
            selenium, live_server_path, categories, [account_foo], from_date, to_date,
        )

        elements = selenium.find_elements_by_xpath("//table/tbody/tr/td")
        columns = 4
        assert len(elements) == (1 + months) * columns

    def test_table_footer(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        category_factory: Callable[..., Category],
        account_foo: Account,
        transaction_foo: Transaction,
    ) -> None:
        categories = [
            category_factory(name="category_a"),
            category_factory(name="category_b"),
        ]
        selenium = authenticate_selenium(user=user_foo)
        self.report_category_balance(
            selenium, live_server_path, categories, [account_foo]
        )

        elements = selenium.find_elements_by_xpath("//table/tfoot/tr/th")
        columns = 4
        assert len(elements) == columns

    def report_category_balance(
        self,
        selenium: WebDriver,
        live_server_path: Callable[[str], str],
        categories: List[Category],
        accounts: List[Account],
        from_date: Optional[datetime.date] = None,
        to_date: Optional[datetime.date] = None,
    ) -> None:
        if from_date is None:
            from_date = datetime.date.today()
        if to_date is None:
            to_date = datetime.date.today()
        url = live_server_path(reverse("reports:report_category_balance"))
        selenium.get(url)
        select = Select(selenium.find_element_by_name("categories"))
        for c in categories:
            select.select_by_visible_text(c.name)
        select = Select(selenium.find_element_by_name("accounts"))
        for account in accounts:
            select.select_by_visible_text(account.name)
        element = selenium.find_element_by_name("from_date")
        element.send_keys(from_date.isoformat())
        element = selenium.find_element_by_name("to_date")
        element.send_keys(to_date.isoformat())
        element = selenium.find_element_by_xpath('//button[@type="submit"]')
        element.click()


class TestNavigationBar:
    def test_authenticated_budget_links(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.open_page_with_navigation_bar(selenium, live_server_path)

        elements = selenium.find_elements_by_xpath(
            '//nav/div[@id="navbarNav"]/ul[@id="budgetActions"]/li/a'
        )
        assert elements[0].text == "Home"
        assert elements[0].get_attribute("href") == live_server_path(
            reverse("budget_index")
        )
        assert elements[1].text == "Connections"
        assert elements[1].get_attribute("href") == live_server_path(
            reverse("connections:connection_list")
        )
        assert elements[2].text == "Accounts"
        assert elements[2].get_attribute("href") == live_server_path(
            reverse("accounts:account_list")
        )
        assert elements[3].text == "Transactions"
        assert elements[3].get_attribute("href") == live_server_path(
            reverse("transactions:transaction_list")
        )
        assert elements[4].text == "Categories"
        assert elements[4].get_attribute("href") == live_server_path(
            reverse("categories:category_list")
        )
        assert elements[5].text == "Income"
        assert elements[5].get_attribute("href") == live_server_path(
            reverse("reports:report_income")
        )
        assert elements[6].text == "Balance"
        assert elements[6].get_attribute("href") == live_server_path(
            reverse("reports:report_balance")
        )
        assert elements[7].text == "Category Balance"
        assert elements[7].get_attribute("href") == live_server_path(
            reverse("reports:report_category_balance")
        )

    def test_not_authenticated_budget_links(
        self, selenium: WebDriver, live_server_path: Callable[[str], str],
    ) -> None:
        self.open_page_with_navigation_bar(selenium, live_server_path)

        elements = selenium.find_elements_by_xpath(
            '//nav/div[@id="navbarNav"]/ul[@id="budgetActions"]/li/a'
        )
        assert len(elements) == 0

    def test_authenticated_profile_links(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.open_page_with_navigation_bar(selenium, live_server_path)

        elements = selenium.find_elements_by_xpath(
            '//nav/div[@id="navbarNav"]/ul[@id="profileActions"]/li/a'
        )
        assert elements[0].text == "User: foo"
        assert elements[0].get_attribute("href") == live_server_path(reverse("profile"))
        assert elements[1].text == "Logout"
        assert elements[1].get_attribute("href") == live_server_path(reverse("logout"))

    def test_not_authenticated_profile_links(
        self, selenium: WebDriver, live_server_path: Callable[[str], str],
    ) -> None:
        self.open_page_with_navigation_bar(selenium, live_server_path)

        elements = selenium.find_elements_by_xpath(
            '//nav/div[@id="navbarNav"]/ul[@id="profileActions"]/li/a'
        )
        assert elements[0].text == "Login"
        assert elements[0].get_attribute("href") == live_server_path(reverse("login"))
        assert elements[1].text == "Try it Free"
        assert elements[1].get_attribute("href") == live_server_path(reverse("signup"))

    def open_page_with_navigation_bar(
        self, selenium: WebDriver, live_server_path: Callable[[str], str],
    ) -> None:
        url = live_server_path(reverse("login"))
        selenium.get(url)


class TestPagination:
    def test_single_page(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        transaction_factory: Callable[..., Transaction],
    ) -> None:
        number_of_pages = 1
        paginate_by = 25
        for _ in range(number_of_pages * paginate_by):
            transaction_factory(user=user_foo)

        base_url = live_server_path(reverse("transactions:transaction_list"))
        url = base_url

        selenium = authenticate_selenium(user=user_foo)
        selenium.get(url)

        elements = selenium.find_elements_by_xpath(
            '//nav/ul[contains(@class, "pagination")]/li/a'
        )
        assert elements[0].text == "Previous"
        assert elements[0].get_attribute("href") == url + "#"
        assert elements[1].text == "1"
        assert elements[1].get_attribute("href") == base_url + "?page=1"
        assert elements[2].text == "Next"
        assert elements[2].get_attribute("href") == url + "#"

    def test_previous_page(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        transaction_factory: Callable[..., Transaction],
    ) -> None:
        number_of_pages = 2
        paginate_by = 25
        for _ in range(number_of_pages * paginate_by):
            transaction_factory(user=user_foo)

        base_url = live_server_path(reverse("transactions:transaction_list"))
        url = base_url + "?page=2"

        selenium = authenticate_selenium(user=user_foo)
        selenium.get(url)

        elements = selenium.find_elements_by_xpath(
            '//nav/ul[contains(@class, "pagination")]/li/a'
        )
        assert elements[0].text == "Previous"
        assert elements[0].get_attribute("href") == base_url + "?page=1"
        assert elements[1].text == "1"
        assert elements[1].get_attribute("href") == base_url + "?page=1"
        assert elements[2].text == "2"
        assert elements[2].get_attribute("href") == base_url + "?page=2"
        assert elements[3].text == "Next"
        assert elements[3].get_attribute("href") == url + "#"

    def test_next_page(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        transaction_factory: Callable[..., Transaction],
    ) -> None:
        number_of_pages = 2
        paginate_by = 25
        for _ in range(number_of_pages * paginate_by):
            transaction_factory(user=user_foo)

        base_url = live_server_path(reverse("transactions:transaction_list"))
        url = base_url + "?page=1"

        selenium = authenticate_selenium(user=user_foo)
        selenium.get(url)

        elements = selenium.find_elements_by_xpath(
            '//nav/ul[contains(@class, "pagination")]/li/a'
        )
        assert elements[0].text == "Previous"
        assert elements[0].get_attribute("href") == url + "#"
        assert elements[1].text == "1"
        assert elements[1].get_attribute("href") == base_url + "?page=1"
        assert elements[2].text == "2"
        assert elements[2].get_attribute("href") == base_url + "?page=2"
        assert elements[3].text == "Next"
        assert elements[3].get_attribute("href") == base_url + "?page=2"

    def test_query_string_without_page(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        transaction_factory: Callable[..., Transaction],
    ) -> None:
        number_of_pages = 2
        paginate_by = 25
        for _ in range(number_of_pages * paginate_by):
            transaction_factory(user=user_foo)

        base_url = live_server_path(reverse("transactions:transaction_list"))
        query_string = "min_amount=100&max_amount=200"
        url = base_url + "?" + query_string

        selenium = authenticate_selenium(user=user_foo)
        selenium.get(url)

        elements = selenium.find_elements_by_xpath(
            '//nav/ul[contains(@class, "pagination")]/li/a'
        )
        assert elements[0].text == "Previous"
        assert elements[0].get_attribute("href") == url + "#"
        assert elements[1].text == "1"
        assert elements[1].get_attribute("href") == base_url + "?page=1&" + query_string
        assert elements[2].text == "2"
        assert elements[2].get_attribute("href") == base_url + "?page=2&" + query_string
        assert elements[3].text == "Next"
        assert elements[3].get_attribute("href") == base_url + "?page=2&" + query_string

    def test_query_string_with_page(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        transaction_factory: Callable[..., Transaction],
    ) -> None:
        number_of_pages = 2
        paginate_by = 25
        for _ in range(number_of_pages * paginate_by):
            transaction_factory(user=user_foo)

        base_url = live_server_path(reverse("transactions:transaction_list"))
        query_string = "min_amount=100&max_amount=200"
        url = base_url + "?page=1&" + query_string

        selenium = authenticate_selenium(user=user_foo)
        selenium.get(url)

        elements = selenium.find_elements_by_xpath(
            '//nav/ul[contains(@class, "pagination")]/li/a'
        )
        assert elements[0].text == "Previous"
        assert elements[0].get_attribute("href") == url + "#"
        assert elements[1].text == "1"
        assert elements[1].get_attribute("href") == base_url + "?page=1&" + query_string
        assert elements[2].text == "2"
        assert elements[2].get_attribute("href") == base_url + "?page=2&" + query_string
        assert elements[3].text == "Next"
        assert elements[3].get_attribute("href") == base_url + "?page=2&" + query_string
