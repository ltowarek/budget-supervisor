import pytest
import datetime
from django.shortcuts import reverse
from django.utils.dateparse import parse_date
from django.utils.formats import date_format
from budget.models import Connection, Account, Transaction
from saltedge_wrapper.factory import connections_api
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


pytestmark = pytest.mark.selenium


class TestIndex:
    pass


class TestConnectionList:
    def test_menu(self, authenticate_selenium, live_server_path, user_foo):
        selenium = authenticate_selenium(user=user_foo)
        url = live_server_path(reverse("connections:connection_list"))
        selenium.get(url)

        elements = selenium.find_elements_by_xpath('//ul[@id="menu"]/li/a')
        assert len(elements) == 2
        assert elements[0].text == "Create"
        assert elements[0].get_attribute("href") == live_server_path(
            reverse("connections:connection_create")
        )
        assert elements[1].text == "Import"
        assert elements[1].get_attribute("href") == live_server_path(
            reverse("connections:connection_import")
        )

    def test_table_header(self, authenticate_selenium, live_server_path, user_foo):
        selenium = authenticate_selenium(user=user_foo)
        url = live_server_path(reverse("connections:connection_list"))
        selenium.get(url)

        elements = selenium.find_elements_by_xpath("//table/thead/tr/th")
        assert len(elements) == 3
        assert elements[0].text == "ID"
        assert elements[1].text == "Provider"
        assert elements[2].text == "Actions"

    def test_table_body(
        self, authenticate_selenium, live_server_path, connection_factory, user_foo,
    ):
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

            actions = cells[2].find_elements_by_xpath(".//ul/li/a")
            assert actions[0].text == "Update"
            assert actions[0].get_attribute("href") == live_server_path(
                reverse("connections:connection_update", kwargs={"pk": connection.pk})
            )
            assert actions[1].text == "Delete"
            assert actions[1].get_attribute("href") == live_server_path(
                reverse("connections:connection_delete", kwargs={"pk": connection.pk})
            )

    def test_pagination(self, authenticate_selenium, live_server_path, user_foo):
        selenium = authenticate_selenium(user=user_foo)
        url = live_server_path(reverse("connections:connection_list"))
        selenium.get(url)

        elements = selenium.find_elements_by_class_name("pagination")
        assert elements


@pytest.fixture
def remove_temporary_connections(predefined_saltedge_connection, predefined_user):
    Connection.objects.import_from_saltedge(
        predefined_user, predefined_user.profile.external_id, connections_api()
    )
    yield
    new_connections = Connection.objects.import_from_saltedge(
        predefined_user, predefined_user.profile.external_id, connections_api()
    )
    for connection in new_connections:
        Connection.objects.remove_from_saltedge(connection, connections_api())


class TestConnectionCreate:
    def test_saltedge_connect_session_creation(
        self,
        authenticate_selenium,
        live_server_path,
        predefined_profile,
        remove_temporary_connections,
    ):
        selenium = authenticate_selenium(user=predefined_profile.user)
        self.create_saltedge_connection(selenium, live_server_path)
        assert selenium.current_url == live_server_path(
            reverse("connections:connection_import")
        )

    def test_cant_create_connection_if_external_synchronization_is_disabled(
        self, authenticate_selenium, live_server_path, user_foo,
    ):
        selenium = authenticate_selenium(user=user_foo)
        url = live_server_path(reverse("connections:connection_create"))
        selenium.get(url)
        element = selenium.find_element_by_id("synchronization")
        assert (
            element.text
            == "Enable external synchronization before creating a connection"
        )

    @classmethod
    def create_saltedge_connection(cls, selenium, live_server_path):
        url = live_server_path(reverse("connections:connection_create"))
        selenium.get(url)
        element = selenium.find_element_by_xpath('//input[@value="Submit"]')
        element.click()
        element = selenium.find_element_by_id("providers-search")
        element.send_keys("Fake Demo Bank")
        element = selenium.find_element_by_class_name("tt-dropdown-menu")
        WebDriverWait(selenium, 5).until(EC.visibility_of(element))
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
        self, authenticate_selenium, live_server_path, user_foo, connection_foo
    ):
        selenium = authenticate_selenium(user=user_foo)
        url = live_server_path(
            reverse("connections:connection_update", kwargs={"pk": connection_foo.pk})
        )
        selenium.get(url)
        element = selenium.find_element_by_xpath('//input[@value="Submit"]')
        element.click()
        assert True


class TestConnectionDelete:
    def test_connection_is_deleted_internally(
        self, authenticate_selenium, live_server_path, user_foo, connection_foo
    ):
        selenium = authenticate_selenium(user=user_foo)
        self.delete_connection(selenium, live_server_path, connection_foo)
        assert Connection.objects.filter(user=user_foo).count() == 0

    def test_connection_is_deleted_externally(self):
        # TODO: There is a need to create SaltEdge connection programatically without a need for Selenium
        assert True

    def test_redirect(
        self, authenticate_selenium, live_server_path, user_foo, connection_foo
    ):
        selenium = authenticate_selenium(user=user_foo)
        self.delete_connection(selenium, live_server_path, connection_foo)
        assert selenium.current_url == live_server_path(
            reverse("connections:connection_list")
        )

    def delete_connection(self, selenium, live_server_path, connection):
        url = live_server_path(
            reverse("connections:connection_delete", kwargs={"pk": connection.pk})
        )
        selenium.get(url)
        element = selenium.find_element_by_xpath('//input[@value="Yes, delete."]')
        element.click()


class TestConnectionImport:
    def test_connection_is_imported(
        self,
        authenticate_selenium,
        live_server_path,
        predefined_profile,
        predefined_saltedge_connection,
    ):
        selenium = authenticate_selenium(user=predefined_profile.user)
        self.import_connections(selenium, live_server_path)
        connections = Connection.objects.filter(user=predefined_profile.user)
        assert connections.count() == 1
        assert str(connections[0].external_id) == predefined_saltedge_connection.id

    def test_redirect(
        self,
        authenticate_selenium,
        live_server_path,
        predefined_profile,
        predefined_saltedge_connection,
    ):
        selenium = authenticate_selenium(user=predefined_profile.user)
        self.import_connections(selenium, live_server_path)
        assert selenium.current_url == live_server_path(
            reverse("connections:connection_list")
        )

    def test_cant_import_connections_if_external_synchronization_is_disabled(
        self, authenticate_selenium, live_server_path, user_foo,
    ):
        selenium = authenticate_selenium(user=user_foo)
        url = live_server_path(reverse("connections:connection_import"))
        selenium.get(url)
        element = selenium.find_element_by_id("synchronization")
        assert (
            element.text
            == "Enable external synchronization before importing connections"
        )

    def import_connections(self, selenium, live_server_path):
        url = live_server_path(reverse("connections:connection_import"))
        selenium.get(url)
        element = selenium.find_element_by_xpath('//input[@value="Import"]')
        element.click()


class TestAccountList:
    def test_menu(self, authenticate_selenium, live_server_path, user_foo):
        selenium = authenticate_selenium(user=user_foo)
        url = live_server_path(reverse("accounts:account_list"))
        selenium.get(url)

        elements = selenium.find_elements_by_xpath('//ul[@id="menu"]/li/a')
        assert len(elements) == 2
        assert elements[0].text == "Create"
        assert elements[0].get_attribute("href") == live_server_path(
            reverse("accounts:account_create")
        )
        assert elements[1].text == "Import"
        assert elements[1].get_attribute("href") == live_server_path(
            reverse("accounts:account_import")
        )

    def test_table_header(self, authenticate_selenium, live_server_path, user_foo):
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
        self, authenticate_selenium, live_server_path, account_factory, user_foo,
    ):
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

            actions = cells[3].find_elements_by_xpath(".//ul/li/a")
            assert actions[0].text == "Update"
            assert actions[0].get_attribute("href") == live_server_path(
                reverse("accounts:account_update", kwargs={"pk": account.pk})
            )
            assert actions[1].text == "Delete"
            assert actions[1].get_attribute("href") == live_server_path(
                reverse("accounts:account_delete", kwargs={"pk": account.pk})
            )

    def test_pagination(self, authenticate_selenium, live_server_path, user_foo):
        selenium = authenticate_selenium(user=user_foo)
        url = live_server_path(reverse("accounts:account_list"))
        selenium.get(url)

        elements = selenium.find_elements_by_class_name("pagination")
        assert elements


class TestAccountCreate:
    def test_account_is_created(
        self, authenticate_selenium, live_server_path, user_foo
    ):
        selenium = authenticate_selenium(user=user_foo)
        self.create_account(selenium, live_server_path, "account name", "Cash")
        accounts = Account.objects.filter(user=user_foo)
        assert accounts.count() == 1
        account = accounts[0]
        assert account.name == "account name"
        assert account.account_type == Account.AccountType.CASH

    def test_redirect(self, authenticate_selenium, live_server_path, user_foo):
        selenium = authenticate_selenium(user=user_foo)
        self.create_account(selenium, live_server_path, "account name", "Cash")
        assert selenium.current_url == live_server_path(
            reverse("accounts:account_list")
        )

    def create_account(self, selenium, live_server_path, name, account_type):
        url = live_server_path(reverse("accounts:account_create"))
        selenium.get(url)
        element = selenium.find_element_by_name("name")
        element.send_keys(name)
        select = Select(selenium.find_element_by_name("account_type"))
        select.select_by_visible_text(account_type)
        element = selenium.find_element_by_xpath('//input[@value="Submit"]')
        element.click()


class TestAccountUpdate:
    def test_account_is_updated(
        self, authenticate_selenium, live_server_path, user_foo, account_foo
    ):
        selenium = authenticate_selenium(user=user_foo)
        self.update_account(
            selenium, live_server_path, account_foo, "account name", "Cash"
        )
        assert account_foo.name == "account name"
        assert account_foo.account_type == Account.AccountType.CASH

    def test_redirect(
        self, authenticate_selenium, live_server_path, user_foo, account_foo
    ):
        selenium = authenticate_selenium(user=user_foo)
        self.update_account(
            selenium, live_server_path, account_foo, "account name", "Cash"
        )
        assert selenium.current_url == live_server_path(
            reverse("accounts:account_list")
        )

    def update_account(self, selenium, live_server_path, account, name, account_type):
        url = live_server_path(
            reverse("accounts:account_update", kwargs={"pk": account.pk})
        )
        selenium.get(url)
        element = selenium.find_element_by_name("name")
        element.clear()
        element.send_keys(name)
        select = Select(selenium.find_element_by_name("account_type"))
        select.select_by_visible_text(account_type)
        element = selenium.find_element_by_xpath('//input[@value="Submit"]')
        element.click()
        account.refresh_from_db()


class TestAccountDelete:
    def test_account_is_deleted(
        self, authenticate_selenium, live_server_path, user_foo, account_foo
    ):
        selenium = authenticate_selenium(user=user_foo)
        self.delete_account(selenium, live_server_path, account_foo)
        assert Account.objects.filter(user=user_foo).count() == 0

    def test_related_transactions_are_deleted(
        self,
        authenticate_selenium,
        live_server_path,
        user_foo,
        account_foo,
        transaction_factory,
    ):
        number_of_transactions = 20
        for i in range(number_of_transactions):
            transaction_factory()
        selenium = authenticate_selenium(user=user_foo)
        self.delete_account(selenium, live_server_path, account_foo)
        assert Transaction.objects.filter(user=user_foo).count() == 0

    def test_redirect(
        self, authenticate_selenium, live_server_path, user_foo, account_foo
    ):
        selenium = authenticate_selenium(user=user_foo)
        self.delete_account(selenium, live_server_path, account_foo)
        assert selenium.current_url == live_server_path(
            reverse("accounts:account_list")
        )

    def delete_account(self, selenium, live_server_path, account):
        url = live_server_path(
            reverse("accounts:account_delete", kwargs={"pk": account.pk})
        )
        selenium.get(url)
        element = selenium.find_element_by_xpath('//input[@value="Yes, delete."]')
        element.click()


class TestAccountImport:
    def test_accounts_are_imported(
        self,
        authenticate_selenium,
        live_server_path,
        predefined_profile,
        predefined_connection,
    ):
        selenium = authenticate_selenium(user=predefined_profile.user)
        self.import_accounts(selenium, live_server_path, predefined_connection)
        accounts = Account.objects.filter(user=predefined_profile.user)
        assert accounts.count() == 5
        for account in accounts:
            assert account.external_id is not None

    def test_redirect(
        self,
        authenticate_selenium,
        live_server_path,
        predefined_profile,
        predefined_connection,
    ):
        selenium = authenticate_selenium(user=predefined_profile.user)
        self.import_accounts(selenium, live_server_path, predefined_connection)
        assert selenium.current_url == live_server_path(
            reverse("accounts:account_list")
        )

    def test_cant_import_accounts_if_external_synchronization_is_disabled(
        self, authenticate_selenium, live_server_path, user_foo,
    ):
        selenium = authenticate_selenium(user=user_foo)
        url = live_server_path(reverse("accounts:account_import"))
        selenium.get(url)
        element = selenium.find_element_by_id("synchronization")
        assert (
            element.text == "Enable external synchronization before importing accounts"
        )

    def import_accounts(self, selenium, live_server_path, connection):
        url = live_server_path(reverse("accounts:account_import"))
        selenium.get(url)
        select = Select(selenium.find_element_by_name("connection"))
        select.select_by_visible_text(connection.provider)
        element = selenium.find_element_by_xpath('//input[@value="Import"]')
        element.click()


class TestTransactionList:
    def test_menu(self, authenticate_selenium, live_server_path, user_foo):
        selenium = authenticate_selenium(user=user_foo)
        url = live_server_path(reverse("transactions:transaction_list"))
        selenium.get(url)

        elements = selenium.find_elements_by_xpath('//ul[@id="menu"]/li/a')
        assert len(elements) == 2
        assert elements[0].text == "Create"
        assert elements[0].get_attribute("href") == live_server_path(
            reverse("transactions:transaction_create")
        )
        assert elements[1].text == "Import"
        assert elements[1].get_attribute("href") == live_server_path(
            reverse("transactions:transaction_import")
        )

    def test_table_header(self, authenticate_selenium, live_server_path, user_foo):
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
        authenticate_selenium,
        live_server_path,
        transaction_factory,
        user_foo,
        category_foo,
        account_foo,
    ):
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

            actions = cells[6].find_elements_by_xpath(".//ul/li/a")
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

    def test_pagination(self, authenticate_selenium, live_server_path, user_foo):
        selenium = authenticate_selenium(user=user_foo)
        url = live_server_path(reverse("transactions:transaction_list"))
        selenium.get(url)

        elements = selenium.find_elements_by_class_name("pagination")
        assert elements


class TestTransactionCreate:
    def test_transaction_is_created(
        self,
        authenticate_selenium,
        live_server_path,
        user_foo,
        category_foo,
        account_foo,
    ):
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
        transactions = Transaction.objects.filter(user=user_foo)
        assert transactions.count() == 1
        transaction = transactions[0]
        assert transaction.date == datetime.date.today()
        assert transaction.amount == 100.0
        assert transaction.payee == "payee"
        assert transaction.category == category_foo
        assert transaction.description == "description"
        assert transaction.account == account_foo

    def test_redirect(
        self,
        authenticate_selenium,
        live_server_path,
        user_foo,
        category_foo,
        account_foo,
    ):
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

    def create_transaction(
        self,
        selenium,
        live_server_path,
        date,
        amount,
        payee,
        category,
        description,
        account,
    ):
        url = live_server_path(reverse("transactions:transaction_create"))
        selenium.get(url)
        element = selenium.find_element_by_name("date")
        element.send_keys(date_format(date, "SHORT_DATE_FORMAT"))
        element = selenium.find_element_by_name("amount")
        element.send_keys(str(amount))
        element = selenium.find_element_by_name("payee")
        element.send_keys(payee)
        select = Select(selenium.find_element_by_name("category"))
        select.select_by_visible_text(category.name)
        element = selenium.find_element_by_name("description")
        element.send_keys(description)
        select = Select(selenium.find_element_by_name("account"))
        select.select_by_visible_text(account.name)
        element = selenium.find_element_by_xpath('//input[@value="Submit"]')
        element.click()


class TestTransactionUpdate:
    def test_transaction_is_updated(
        self,
        authenticate_selenium,
        live_server_path,
        user_foo,
        transaction_foo,
        category_foo,
        account_foo,
    ):
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
        transactions = Transaction.objects.filter(user=user_foo)
        assert transactions.count() == 1
        transaction = transactions[0]
        assert transaction.date == datetime.date.today()
        assert transaction.amount == 100.0
        assert transaction.payee == "payee"
        assert transaction.category == category_foo
        assert transaction.description == "description"
        assert transaction.account == account_foo

    def test_redirect(
        self,
        authenticate_selenium,
        live_server_path,
        user_foo,
        transaction_foo,
        category_foo,
        account_foo,
    ):
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

    def update_transaction(
        self,
        selenium,
        live_server_path,
        transaction,
        date,
        amount,
        payee,
        category,
        description,
        account,
    ):
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
        element = selenium.find_element_by_xpath('//input[@value="Submit"]')
        element.click()
        transaction.refresh_from_db()


class TestTransactionDelete:
    def test_transaction_is_deleted(
        self, authenticate_selenium, live_server_path, user_foo, transaction_foo
    ):
        selenium = authenticate_selenium(user=user_foo)
        self.delete_transaction(selenium, live_server_path, transaction_foo)
        assert Transaction.objects.filter(user=user_foo).count() == 0

    def test_redirect(
        self, authenticate_selenium, live_server_path, user_foo, transaction_foo
    ):
        selenium = authenticate_selenium(user=user_foo)
        self.delete_transaction(selenium, live_server_path, transaction_foo)
        assert selenium.current_url == live_server_path(
            reverse("transactions:transaction_list")
        )

    def delete_transaction(self, selenium, live_server_path, transaction):
        url = live_server_path(
            reverse("transactions:transaction_delete", kwargs={"pk": transaction.pk})
        )
        selenium.get(url)
        element = selenium.find_element_by_xpath('//input[@value="Yes, delete."]')
        element.click()


class TestTransactionImport:
    def test_transactions_are_imported(
        self,
        authenticate_selenium,
        live_server_path,
        predefined_profile,
        predefined_account,
    ):
        selenium = authenticate_selenium(user=predefined_profile.user)
        self.import_transactions(selenium, live_server_path, predefined_account)
        transactions = Transaction.objects.filter(user=predefined_profile.user)
        assert transactions.count() == 17
        for transaction in transactions:
            assert transaction.external_id is not None

    def test_redirect(
        self,
        authenticate_selenium,
        live_server_path,
        predefined_profile,
        predefined_account,
    ):
        selenium = authenticate_selenium(user=predefined_profile.user)
        self.import_transactions(selenium, live_server_path, predefined_account)
        assert selenium.current_url == live_server_path(
            reverse("transactions:transaction_list")
        )

    def test_cant_import_transactions_if_external_synchronization_is_disabled(
        self, authenticate_selenium, live_server_path, user_foo,
    ):
        selenium = authenticate_selenium(user=user_foo)
        url = live_server_path(reverse("transactions:transaction_import"))
        selenium.get(url)
        element = selenium.find_element_by_id("synchronization")
        assert (
            element.text
            == "Enable external synchronization before importing transactions"
        )

    def import_transactions(self, selenium, live_server_path, account):
        url = live_server_path(reverse("transactions:transaction_import"))
        selenium.get(url)
        select = Select(selenium.find_element_by_name("account"))
        select.select_by_visible_text(account.name)
        element = selenium.find_element_by_xpath('//input[@value="Import"]')
        element.click()
