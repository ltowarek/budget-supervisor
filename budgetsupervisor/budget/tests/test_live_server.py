import pytest
from django.shortcuts import reverse
from budget.models import Connection
from saltedge_wrapper.factory import connections_api
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        self,
        authenticate_selenium,
        live_server_path,
        connection_factory,
        predefined_user,
    ):
        number_of_connections = 20
        for i in range(number_of_connections):
            connection_factory(f"provider {i}", user=predefined_user)
        connections = Connection.objects.filter(user=predefined_user).order_by(
            "provider"
        )
        assert len(connections) == number_of_connections

        selenium = authenticate_selenium(user=predefined_user)
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
def remove_temporary_connections(predefined_connection, predefined_user):
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
        WebDriverWait(selenium, 20).until(EC.url_to_be(redirect_url))


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
        assert Connection.objects.filter(user=user_foo).count() == 1
        selenium = authenticate_selenium(user=user_foo)
        url = live_server_path(
            reverse("connections:connection_delete", kwargs={"pk": connection_foo.pk})
        )
        selenium.get(url)
        element = selenium.find_element_by_xpath('//input[@value="Yes, delete."]')
        element.click()
        assert Connection.objects.filter(user=user_foo).count() == 0

    def test_connection_is_deleted_externally(self):
        # TODO: There is a need to create SaltEdge connection programatically without a need for Selenium
        assert True