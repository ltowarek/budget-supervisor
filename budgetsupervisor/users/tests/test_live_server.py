import pytest
from django.shortcuts import reverse
from saltedge_wrapper.factory import customers_api
from users.models import Profile


pytestmark = pytest.mark.selenium


class TestLogin:
    def test_valid_credentials_redirect_to_budget_index(
        self, selenium, live_server_path, user_foo
    ):
        url = live_server_path(reverse("login"))
        selenium.get(url)
        self.login_user(selenium, "foo", "password")
        assert selenium.current_url == live_server_path(reverse("budget_index"))

    def test_invalid_credentials_prints_error_message(self, selenium, live_server_path):
        url = live_server_path(reverse("login"))
        selenium.get(url)
        self.login_user(selenium, "bar", "xyz")
        assert (
            selenium.find_element_by_id("form_errors").text
            == "Your username and password didn't match. Please try again."
        )

    def test_next_redirects_to_requsted_url(self, selenium, live_server_path, user_foo):
        url = live_server_path(reverse("login") + "?next=" + reverse("profile"))
        selenium.get(url)
        self.login_user(selenium, "foo", "password")
        assert selenium.current_url == live_server_path(reverse("profile"))

    def test_not_authenticated_user_accessing_page_is_redirected_to_login_page(
        self, selenium, live_server_path
    ):
        url = live_server_path(reverse("profile"))
        selenium.get(url)
        assert selenium.current_url == live_server_path(
            reverse("login") + "?next=" + reverse("profile")
        )
        assert (
            selenium.find_element_by_id("login_required").text
            == "Please login to see this page."
        )

    def login_user(self, selenium, username, password):
        username_input = selenium.find_element_by_name("username")
        username_input.send_keys(username)
        password_input = selenium.find_element_by_name("password")
        password_input.send_keys(password)
        selenium.find_element_by_xpath('//input[@value="login"]').click()


class TestSignUp:
    def test_sign_up_redirects_to_login_page(self, selenium, live_server_path):
        url = live_server_path(reverse("signup"))
        selenium.get(url)
        self.sign_up_user(selenium, "foo", "Foo Password")
        assert selenium.current_url == live_server_path(reverse("login"))

    def test_existing_user_cant_sign_up_again(
        self, selenium, live_server_path, user_foo
    ):
        url = live_server_path(reverse("signup"))
        selenium.get(url)
        self.sign_up_user(selenium, "foo", "password")
        assert (
            selenium.find_element_by_class_name("errorlist")
            .find_elements_by_tag_name("li")[0]
            .text
            == "A user with that username already exists."
        )

    def sign_up_user(self, selenium, username, password):
        username_input = selenium.find_element_by_name("username")
        username_input.send_keys(username)
        password1_input = selenium.find_element_by_name("password1")
        password1_input.send_keys(password)
        password2_input = selenium.find_element_by_name("password2")
        password2_input.send_keys(password)
        selenium.find_element_by_xpath('//input[@value="Sign Up"]').click()


class TestProfile:
    def test_synchronization_can_be_enabled_if_not_already_enabled(
        self, authenticate_selenium, live_server_path, profile_foo
    ):
        selenium = authenticate_selenium(user=profile_foo.user)
        url = live_server_path(reverse("profile"))
        selenium.get(url)
        element = selenium.find_element_by_id("synchronization")
        assert element.text == "Enable external synchronization"
        assert element.get_attribute("href") == live_server_path(
            reverse("profile_connect")
        )

    def test_synchronization_can_be_disabled_if_already_enabled(
        self, authenticate_selenium, live_server_path, profile_foo_external
    ):
        selenium = authenticate_selenium(user=profile_foo_external.user)
        url = live_server_path(reverse("profile"))
        selenium.get(url)
        element = selenium.find_element_by_id("synchronization")
        assert element.text == "Disable external synchronization"
        assert element.get_attribute("href") == live_server_path(
            reverse("profile_disconnect")
        )

    def test_enable_external_synchronization(
        self, authenticate_selenium, live_server_path, profile_foo
    ):
        selenium = authenticate_selenium(user=profile_foo.user)
        self.enable_external_synchronization(selenium, live_server_path, profile_foo)
        assert profile_foo.external_id is not None
        assert selenium.current_url == live_server_path(reverse("profile"))
        Profile.objects.remove_from_saltedge(profile_foo, customers_api())

    def test_disable_external_synchronization(
        self, authenticate_selenium, live_server_path, profile_foo
    ):
        selenium = authenticate_selenium(user=profile_foo.user)
        Profile.objects.create_in_saltedge(profile_foo, customers_api())
        self.disable_external_synchronization(selenium, live_server_path, profile_foo)
        assert profile_foo.external_id is None
        assert selenium.current_url == live_server_path(reverse("profile"))

    def enable_external_synchronization(self, selenium, live_server_path, profile):
        url = live_server_path(reverse("profile_connect"))
        selenium.get(url)
        selenium.find_element_by_xpath('//input[@value="Submit"]').click()
        profile.refresh_from_db()

    def disable_external_synchronization(self, selenium, live_server_path, profile):
        url = live_server_path(reverse("profile_disconnect"))
        selenium.get(url)
        selenium.find_element_by_xpath('//input[@value="Submit"]').click()
        profile.refresh_from_db()
