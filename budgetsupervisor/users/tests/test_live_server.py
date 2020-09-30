import pytest
from django.shortcuts import reverse


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
