import datetime
from typing import Callable, Iterator, List, Optional

import pytest
import swagger_client as saltedge_client
from budget.models import Account, Category, Connection, Transaction
from budget.services import (
    import_connections_from_saltedge,
    remove_connection_from_saltedge,
)
from django.shortcuts import reverse
from django.utils.dateparse import parse_date
from django.utils.formats import date_format
from saltedge_wrapper.factory import connections_api
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from swagger_client.rest import ApiException
from users.models import Profile, User

pytestmark = pytest.mark.selenium


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
        assert len(elements) == 2
        assert elements[0].text == "Create"
        assert elements[0].get_attribute("href") == live_server_path(
            reverse("connections:connection_create")
        )
        assert elements[1].text == "Import"
        assert elements[1].get_attribute("href") == live_server_path(
            reverse("connections:connection_import")
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
        assert len(elements) == 3
        assert elements[0].text == "ID"
        assert elements[1].text == "Provider"
        assert elements[2].text == "Actions"

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
            assert len(cells) == 3

            assert cells[0].text == str(connection.id)
            assert cells[1].text == connection.provider

            actions = cells[2].find_elements_by_xpath(".//a")
            assert actions[0].text == "Update"
            assert actions[0].get_attribute("href") == live_server_path(
                reverse("connections:connection_update", kwargs={"pk": connection.pk})
            )
            assert actions[1].text == "Delete"
            assert actions[1].get_attribute("href") == live_server_path(
                reverse("connections:connection_delete", kwargs={"pk": connection.pk})
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
    predefined_saltedge_connection: saltedge_client.Connection, predefined_user: User
) -> Iterator[None]:
    import_connections_from_saltedge(
        predefined_user, predefined_user.profile.external_id, connections_api()
    )
    yield
    new_connections = import_connections_from_saltedge(
        predefined_user, predefined_user.profile.external_id, connections_api()
    )
    for connection in new_connections:
        remove_connection_from_saltedge(connection, connections_api())


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
            reverse("connections:connection_import")
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
        cls, selenium: WebDriver, live_server_path: Callable[[str], str]
    ) -> None:
        url = live_server_path(reverse("connections:connection_create"))
        selenium.get(url)
        element = selenium.find_element_by_xpath('//button[@type="submit"]')
        element.click()
        element = selenium.find_element_by_id("providers-search")
        element.send_keys("Fake Demo Bank")
        element = selenium.find_element_by_class_name("tt-dropdown-menu")
        WebDriverWait(selenium, 10).until(EC.visibility_of(element))
        element = selenium.find_element_by_class_name("tt-suggestion")
        element.click()
        element = selenium.find_element_by_name("username")
        element.send_keys("username")
        element = selenium.find_element_by_name("password")
        element.send_keys("secret")
        element = selenium.find_element_by_xpath('//input[@value="Proceed"]')
        element.click()
        element = selenium.find_element_by_xpath('//input[@value="Confirm"]')
        element.click()
        redirect_url = live_server_path(reverse("connections:connection_import"))
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
        self.update_category(selenium, live_server_path, connection_foo)
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
        self.update_category(selenium, live_server_path, connection_foo)
        messages = [
            m.text
            for m in selenium.find_elements_by_xpath('//div[contains(@class, "alert")]')
        ]
        assert any(
            "Connection was updated successfully" in message for message in messages
        )

    def update_category(
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


@pytest.fixture
def connection_external_factory(
    remove_temporary_connections: Callable[..., None],
) -> Callable[..., Connection]:
    def f(
        selenium: WebDriver, live_server_path: Callable[[str], str], profile: Profile
    ) -> Connection:
        import_connections_from_saltedge(
            profile.user, profile.external_id, connections_api()
        )
        # There is no other way to create connection than using Selenium
        TestConnectionCreate.create_saltedge_connection(selenium, live_server_path)
        new_connections = import_connections_from_saltedge(
            profile.user, profile.external_id, connections_api()
        )
        return new_connections[0]

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


class TestConnectionImport:
    def test_connection_is_imported(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        predefined_profile: Profile,
        predefined_saltedge_connection: saltedge_client.Connection,
    ) -> None:
        selenium = authenticate_selenium(user=predefined_profile.user)
        self.import_connections(selenium, live_server_path)
        connections = Connection.objects.filter(user=predefined_profile.user)
        assert connections.count() == 1
        assert str(connections[0].external_id) == predefined_saltedge_connection.id

    def test_redirect(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        predefined_profile: Profile,
        predefined_saltedge_connection: saltedge_client.Connection,
    ) -> None:
        selenium = authenticate_selenium(user=predefined_profile.user)
        self.import_connections(selenium, live_server_path)
        assert selenium.current_url == live_server_path(
            reverse("connections:connection_list")
        )

    def test_message(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        predefined_profile: Profile,
        predefined_saltedge_connection: saltedge_client.Connection,
    ) -> None:
        selenium = authenticate_selenium(user=predefined_profile.user)
        self.import_connections(selenium, live_server_path)
        messages = [
            m.text
            for m in selenium.find_elements_by_xpath('//div[contains(@class, "alert")]')
        ]
        assert any(
            "Connections were imported successfully: 1" in message
            for message in messages
        )

    def test_cant_import_connections_if_external_synchronization_is_disabled(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        url = live_server_path(reverse("connections:connection_import"))
        selenium.get(url)
        element = selenium.find_element_by_id("synchronization")
        assert (
            element.text
            == "Enable external synchronization before importing connections"
        )

    def import_connections(
        self, selenium: WebDriver, live_server_path: Callable[[str], str]
    ) -> None:
        url = live_server_path(reverse("connections:connection_import"))
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
        assert len(elements) == 2
        assert elements[0].text == "Create"
        assert elements[0].get_attribute("href") == live_server_path(
            reverse("accounts:account_create")
        )
        assert elements[1].text == "Import"
        assert elements[1].get_attribute("href") == live_server_path(
            reverse("accounts:account_import")
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
        assert len(elements) == 4
        assert elements[0].text == "ID"
        assert elements[1].text == "Name"
        assert elements[2].text == "Type"
        assert elements[3].text == "Actions"

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
            assert len(cells) == 4

            assert cells[0].text == str(account.id)
            assert cells[1].text == account.name
            assert cells[2].text == account.get_account_type_display()

            actions = cells[3].find_elements_by_xpath(".//a")
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


class TestAccountCreate:
    def test_account_is_created(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.create_account(selenium, live_server_path, "account name", "Cash")
        account = Account.objects.filter(user=user_foo).last()
        assert account.name == "account name"
        assert account.account_type == Account.AccountType.CASH

    def test_redirect(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.create_account(selenium, live_server_path, "account name", "Cash")
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
        self.create_account(selenium, live_server_path, "account name", "Cash")
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
        account_type: str,
    ) -> None:
        url = live_server_path(reverse("accounts:account_create"))
        selenium.get(url)
        element = selenium.find_element_by_name("name")
        element.send_keys(name)
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
            selenium, live_server_path, account_foo, "account name", "Cash"
        )
        assert account_foo.name == "account name"
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
            selenium, live_server_path, account_foo, "account name", "Cash"
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
            selenium, live_server_path, account_foo, "account name", "Cash"
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
        account_type: str,
    ) -> None:
        url = live_server_path(
            reverse("accounts:account_update", kwargs={"pk": account.pk})
        )
        selenium.get(url)
        element = selenium.find_element_by_name("name")
        element.clear()
        element.send_keys(name)
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


class TestAccountImport:
    def test_accounts_are_imported(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        predefined_profile: Profile,
        predefined_connection: Connection,
    ) -> None:
        selenium = authenticate_selenium(user=predefined_profile.user)
        self.import_accounts(selenium, live_server_path, predefined_connection)
        accounts = Account.objects.filter(user=predefined_profile.user)
        assert accounts.count() == 5
        for account in accounts:
            assert account.external_id is not None

    def test_accounts_are_not_duplicated(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        predefined_profile: Profile,
        predefined_connection: Connection,
    ) -> None:
        selenium = authenticate_selenium(user=predefined_profile.user)
        self.import_accounts(selenium, live_server_path, predefined_connection)
        count_pre = Account.objects.filter(user=predefined_profile.user).count()
        self.import_accounts(selenium, live_server_path, predefined_connection)
        count_post = Account.objects.filter(user=predefined_profile.user).count()
        assert count_pre == count_post

    def test_redirect(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        predefined_profile: Profile,
        predefined_connection: Connection,
    ) -> None:
        selenium = authenticate_selenium(user=predefined_profile.user)
        self.import_accounts(selenium, live_server_path, predefined_connection)
        assert selenium.current_url == live_server_path(
            reverse("accounts:account_list")
        )

    def test_message(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        predefined_profile: Profile,
        predefined_connection: Connection,
    ) -> None:
        selenium = authenticate_selenium(user=predefined_profile.user)
        self.import_accounts(selenium, live_server_path, predefined_connection)
        messages = [
            m.text
            for m in selenium.find_elements_by_xpath('//div[contains(@class, "alert")]')
        ]
        assert any(
            "Accounts were imported successfully: 5" in message for message in messages
        )

    def test_cant_import_accounts_if_external_synchronization_is_disabled(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        url = live_server_path(reverse("accounts:account_import"))
        selenium.get(url)
        element = selenium.find_element_by_id("synchronization")
        assert (
            element.text == "Enable external synchronization before importing accounts"
        )

    def import_accounts(
        self,
        selenium: WebDriver,
        live_server_path: Callable[[str], str],
        connection: Connection,
    ) -> None:
        url = live_server_path(reverse("accounts:account_import"))
        selenium.get(url)
        select = Select(selenium.find_element_by_name("connection"))
        select.select_by_visible_text(connection.provider)
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
        assert len(elements) == 2
        assert elements[0].text == "Create"
        assert elements[0].get_attribute("href") == live_server_path(
            reverse("transactions:transaction_create")
        )
        assert elements[1].text == "Import"
        assert elements[1].get_attribute("href") == live_server_path(
            reverse("transactions:transaction_import")
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
        assert elements[0].text == "ID"
        assert elements[1].text == "Date"
        assert elements[2].text == "Amount"
        assert elements[3].text == "Payee"
        assert elements[4].text == "Category"
        assert elements[5].text == "Description"
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

            assert cells[0].text == str(transaction.id)
            # parse_date does not support SHORT_DATE_FORMAT
            assert parse_date(cells[1].text) is None
            assert cells[2].text == str(transaction.amount)
            assert cells[3].text == transaction.payee
            assert cells[4].text == str(transaction.category)
            assert cells[5].text == transaction.description

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
        element.send_keys(date_format(date, "SHORT_DATE_FORMAT"))
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
        element.send_keys(date_format(date, "SHORT_DATE_FORMAT"))
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


class TestTransactionImport:
    def test_transactions_are_imported(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        predefined_profile: Profile,
        predefined_account: Account,
    ) -> None:
        selenium = authenticate_selenium(user=predefined_profile.user)
        self.import_transactions(selenium, live_server_path, predefined_account)
        transactions = Transaction.objects.filter(user=predefined_profile.user)
        assert transactions.count() == 17
        for transaction in transactions:
            assert transaction.external_id is not None

    def test_transactions_are_not_duplicated(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        predefined_profile: Profile,
        predefined_account: Account,
    ) -> None:
        selenium = authenticate_selenium(user=predefined_profile.user)
        self.import_transactions(selenium, live_server_path, predefined_account)
        count_pre = Transaction.objects.filter(user=predefined_profile.user).count()
        self.import_transactions(selenium, live_server_path, predefined_account)
        count_post = Transaction.objects.filter(user=predefined_profile.user).count()
        assert count_pre == count_post

    def test_redirect(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        predefined_profile: Profile,
        predefined_account: Account,
    ) -> None:
        selenium = authenticate_selenium(user=predefined_profile.user)
        self.import_transactions(selenium, live_server_path, predefined_account)
        assert selenium.current_url == live_server_path(
            reverse("transactions:transaction_list")
        )

    def test_message(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        predefined_profile: Profile,
        predefined_account: Account,
    ) -> None:
        selenium = authenticate_selenium(user=predefined_profile.user)
        self.import_transactions(selenium, live_server_path, predefined_account)
        messages = [
            m.text
            for m in selenium.find_elements_by_xpath('//div[contains(@class, "alert")]')
        ]
        assert any(
            "Transactions were imported successfully: 17" in message
            for message in messages
        )

    def test_cant_import_transactions_if_external_synchronization_is_disabled(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        url = live_server_path(reverse("transactions:transaction_import"))
        selenium.get(url)
        element = selenium.find_element_by_id("synchronization")
        assert (
            element.text
            == "Enable external synchronization before importing transactions"
        )

    def import_transactions(
        self,
        selenium: WebDriver,
        live_server_path: Callable[[str], str],
        account: Account,
    ) -> None:
        url = live_server_path(reverse("transactions:transaction_import"))
        selenium.get(url)
        select = Select(selenium.find_element_by_name("account"))
        select.select_by_visible_text(account.name)
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
        assert len(elements) == 3
        assert elements[0].text == "ID"
        assert elements[1].text == "Name"
        assert elements[2].text == "Actions"

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
            assert len(cells) == 3

            assert cells[0].text == str(category.id)
            assert cells[1].text == category.name

            actions = cells[2].find_elements_by_xpath(".//a")
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
        assert len(elements) == 2
        assert elements[0].text == "Category"
        assert elements[1].text == "Balance"

    def test_table_body(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        account_factory: Callable[..., Account],
        category_factory: Callable[..., Category],
        transaction_factory: Callable[..., Transaction],
    ) -> None:
        number_of_accounts = 10
        for i in range(number_of_accounts):
            account_factory(name=f"account {i}", user=user_foo)
        accounts = Account.objects.filter(user=user_foo)
        selected_accounts = accounts[:5]

        number_of_categories = 2
        category_even = category_factory(name="even")
        category_odd = category_factory(name="odd")

        from_date = datetime.date.today() - datetime.timedelta(days=5)
        to_date = datetime.date.today() - datetime.timedelta(days=2)

        transaction_start_date = from_date - datetime.timedelta(days=2)
        number_of_transactions = 10
        for j in range(number_of_accounts):
            for i in range(number_of_transactions):
                category = category_even if i % 2 == 0 else category_odd
                transaction_factory(
                    description=f"transaction {j + i}",
                    amount=float(i),
                    date=transaction_start_date + datetime.timedelta(days=i),
                    account=accounts[j],
                    category=category,
                    user=user_foo,
                )

        selenium = authenticate_selenium(user=user_foo)
        self.report_balance(
            selenium, live_server_path, selected_accounts, from_date, to_date
        )

        elements = selenium.find_elements_by_xpath("//table/tbody/tr")
        total = 1
        assert len(elements) == number_of_categories + total

    def test_table_body_null_categories_are_included(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        account_foo: Account,
        transaction_foo: Transaction,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.report_balance(selenium, live_server_path, [account_foo])

        elements = selenium.find_elements_by_xpath("//table/tbody/tr")
        assert len(elements) == 2
        assert elements[0].find_elements_by_xpath(".//td")[0].text == "None"
        assert elements[1].find_elements_by_xpath(".//td")[0].text == "Total"

    def report_balance(
        self,
        selenium: WebDriver,
        live_server_path: Callable[[str], str],
        accounts: List[Account],
        from_date: datetime.date = None,
        to_date: datetime.date = None,
    ) -> None:
        url = live_server_path(reverse("reports:report_balance"))
        selenium.get(url)
        select = Select(selenium.find_element_by_name("accounts"))
        for account in accounts:
            select.select_by_visible_text(account.name)
        if from_date:
            element = selenium.find_element_by_name("from_date")
            element.send_keys(date_format(from_date, "SHORT_DATE_FORMAT"))
        if to_date:
            element = selenium.find_element_by_name("to_date")
            element.send_keys(date_format(to_date, "SHORT_DATE_FORMAT"))
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
        assert elements[5].text == "Balance"
        assert elements[5].get_attribute("href") == live_server_path(
            reverse("reports:report_balance")
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
