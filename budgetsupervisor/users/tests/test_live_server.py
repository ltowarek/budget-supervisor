from typing import Callable, Iterable

import pytest
from budget.models import Account, Connection, Transaction
from django.shortcuts import reverse
from saltedge_wrapper.factory import customers_api
from selenium.webdriver.firefox.webdriver import WebDriver
from users.models import Profile, User

pytestmark = pytest.mark.selenium


class TestLogin:
    def test_valid_credentials_redirect_to_budget_index(
        self,
        selenium: WebDriver,
        live_server_path: Callable[[str], str],
        user_foo: User,
    ) -> None:
        url = live_server_path(reverse("login"))
        selenium.get(url)
        self.login_user(selenium, "foo", "password")
        assert selenium.current_url == live_server_path(reverse("budget_index"))

    def test_invalid_credentials_prints_error_message(
        self, selenium: WebDriver, live_server_path: Callable[[str], str]
    ) -> None:
        url = live_server_path(reverse("login"))
        selenium.get(url)
        self.login_user(selenium, "bar", "xyz")
        assert (
            selenium.find_element_by_id("form_errors").text
            == "Your username and password didn't match. Please try again."
        )

    def test_next_redirects_to_requsted_url(
        self,
        selenium: WebDriver,
        live_server_path: Callable[[str], str],
        user_foo: User,
    ) -> None:
        url = live_server_path(reverse("login") + "?next=" + reverse("profile"))
        selenium.get(url)
        self.login_user(selenium, "foo", "password")
        assert selenium.current_url == live_server_path(reverse("profile"))

    def test_not_authenticated_user_accessing_page_is_redirected_to_login_page(
        self, selenium: WebDriver, live_server_path: Callable[[str], str]
    ) -> None:
        url = live_server_path(reverse("profile"))
        selenium.get(url)
        assert selenium.current_url == live_server_path(
            reverse("login") + "?next=" + reverse("profile")
        )
        assert (
            selenium.find_element_by_id("login_required").text
            == "Please login to see this page."
        )

    def login_user(self, selenium: WebDriver, username: str, password: str) -> None:
        username_input = selenium.find_element_by_name("username")
        username_input.send_keys(username)
        password_input = selenium.find_element_by_name("password")
        password_input.send_keys(password)
        selenium.find_element_by_xpath('//input[@value="login"]').click()


class TestSignUp:
    def test_sign_up_redirects_to_login_page(
        self, selenium: WebDriver, live_server_path: Callable[[str], str]
    ) -> None:
        url = live_server_path(reverse("signup"))
        selenium.get(url)
        self.sign_up_user(selenium, "foo", "Foo Password")
        assert selenium.current_url == live_server_path(reverse("login"))

    def test_existing_user_cant_sign_up_again(
        self,
        selenium: WebDriver,
        live_server_path: Callable[[str], str],
        user_foo: User,
    ) -> None:
        url = live_server_path(reverse("signup"))
        selenium.get(url)
        self.sign_up_user(selenium, "foo", "password")
        assert (
            selenium.find_element_by_class_name("errorlist")
            .find_elements_by_tag_name("li")[0]
            .text
            == "A user with that username already exists."
        )

    def sign_up_user(self, selenium: WebDriver, username: str, password: str) -> None:
        username_input = selenium.find_element_by_name("username")
        username_input.send_keys(username)
        password1_input = selenium.find_element_by_name("password1")
        password1_input.send_keys(password)
        password2_input = selenium.find_element_by_name("password2")
        password2_input.send_keys(password)
        selenium.find_element_by_xpath('//input[@value="Sign Up"]').click()


class TestProfileUpdate:
    def test_redirect(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        profile_foo: Profile,
    ) -> None:
        selenium = authenticate_selenium(user=profile_foo.user)
        self.update_profile(selenium, live_server_path, profile_foo)
        assert selenium.current_url == live_server_path(reverse("profile"))

    def test_message(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        profile_foo: Profile,
    ) -> None:
        selenium = authenticate_selenium(user=profile_foo.user)
        self.update_profile(selenium, live_server_path, profile_foo)
        messages = [
            m.text
            for m in selenium.find_elements_by_xpath('//ul[@class="messages"]/li')
        ]
        assert "Profile was updated successfully" in messages

    def update_profile(
        self,
        selenium: WebDriver,
        live_server_path: Callable[[str], str],
        profile: Profile,
    ) -> None:
        url = live_server_path(reverse("profile"))
        selenium.get(url)
        element = selenium.find_element_by_xpath('//input[@value="Submit"]')
        element.click()
        profile.refresh_from_db()

    def test_synchronization_can_be_enabled_if_not_already_enabled(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        profile_foo: Profile,
    ) -> None:
        selenium = authenticate_selenium(user=profile_foo.user)
        url = live_server_path(reverse("profile"))
        selenium.get(url)
        element = selenium.find_element_by_id("synchronization")
        assert element.text == "Enable external synchronization"
        assert element.get_attribute("href") == live_server_path(
            reverse("profile_connect")
        )

    def test_synchronization_can_be_disabled_if_already_enabled(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        profile_foo_external: Profile,
    ) -> None:
        selenium = authenticate_selenium(user=profile_foo_external.user)
        url = live_server_path(reverse("profile"))
        selenium.get(url)
        element = selenium.find_element_by_id("synchronization")
        assert element.text == "Disable external synchronization"
        assert element.get_attribute("href") == live_server_path(
            reverse("profile_disconnect")
        )


@pytest.fixture
def remove_temporary_customers() -> Iterable[None]:
    api = customers_api()
    customers_before = api.customers_get().data
    yield
    customers_after = api.customers_get().data
    new_customers = [c for c in customers_after if c not in customers_before]
    for customer in new_customers:
        api.customers_customer_id_delete(customer.id)


class TestProfileConnect:
    def test_profile_is_updated(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        profile_foo: Profile,
        remove_temporary_customers: Callable[[], Iterable[None]],
    ) -> None:
        selenium = authenticate_selenium(user=profile_foo.user)
        self.enable_external_synchronization(selenium, live_server_path, profile_foo)
        assert profile_foo.external_id is not None
        assert selenium.current_url == live_server_path(reverse("profile"))

    def test_redirect(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        profile_foo: Profile,
        remove_temporary_customers: Callable[[], Iterable[None]],
    ) -> None:
        selenium = authenticate_selenium(user=profile_foo.user)
        self.enable_external_synchronization(selenium, live_server_path, profile_foo)
        assert selenium.current_url == live_server_path(reverse("profile"))

    def test_message(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        profile_foo: Profile,
        remove_temporary_customers: Callable[[], Iterable[None]],
    ) -> None:
        selenium = authenticate_selenium(user=profile_foo.user)
        self.enable_external_synchronization(selenium, live_server_path, profile_foo)
        messages = [
            m.text
            for m in selenium.find_elements_by_xpath('//ul[@class="messages"]/li')
        ]
        assert "Profile was connected successfully" in messages

    def enable_external_synchronization(
        self,
        selenium: WebDriver,
        live_server_path: Callable[[str], str],
        profile: Profile,
    ) -> None:
        url = live_server_path(reverse("profile_connect"))
        selenium.get(url)
        selenium.find_element_by_xpath('//input[@value="Submit"]').click()
        profile.refresh_from_db()


class TestProfileDisconnect:
    def test_profile_is_updated(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        profile_foo: Profile,
        remove_temporary_customers: Callable[[], Iterable[None]],
    ) -> None:
        selenium = authenticate_selenium(user=profile_foo.user)
        Profile.objects.create_in_saltedge(profile_foo, customers_api())
        self.disable_external_synchronization(selenium, live_server_path, profile_foo)
        assert profile_foo.external_id is None

    def test_redirect(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        profile_foo: Profile,
        remove_temporary_customers: Callable[[], Iterable[None]],
    ) -> None:
        selenium = authenticate_selenium(user=profile_foo.user)
        Profile.objects.create_in_saltedge(profile_foo, customers_api())
        self.disable_external_synchronization(selenium, live_server_path, profile_foo)
        assert selenium.current_url == live_server_path(reverse("profile"))

    def test_message(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        profile_foo: Profile,
        remove_temporary_customers: Callable[[], Iterable[None]],
    ) -> None:
        selenium = authenticate_selenium(user=profile_foo.user)
        Profile.objects.create_in_saltedge(profile_foo, customers_api())
        self.disable_external_synchronization(selenium, live_server_path, profile_foo)
        messages = [
            m.text
            for m in selenium.find_elements_by_xpath('//ul[@class="messages"]/li')
        ]
        assert "Profile was disconnected successfully" in messages

    def test_connections_deleted(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        profile_foo: Profile,
        connection_foo: Connection,
        remove_temporary_customers: Callable[[], Iterable[None]],
    ) -> None:
        selenium = authenticate_selenium(user=profile_foo.user)
        Profile.objects.create_in_saltedge(profile_foo, customers_api())
        self.disable_external_synchronization(selenium, live_server_path, profile_foo)
        assert not Connection.objects.filter(pk=connection_foo.pk).exists()

    def test_accounts_disconnected(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        profile_foo: Profile,
        account_foo_external: Account,
        remove_temporary_customers: Callable[[], Iterable[None]],
    ) -> None:
        selenium = authenticate_selenium(user=profile_foo.user)
        Profile.objects.create_in_saltedge(profile_foo, customers_api())
        self.disable_external_synchronization(selenium, live_server_path, profile_foo)
        account_foo_external.refresh_from_db()
        assert account_foo_external.external_id is None

    def test_transactions_disconnected(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        profile_foo: Profile,
        transaction_foo_external: Transaction,
        remove_temporary_customers: Callable[[], Iterable[None]],
    ) -> None:
        selenium = authenticate_selenium(user=profile_foo.user)
        Profile.objects.create_in_saltedge(profile_foo, customers_api())
        self.disable_external_synchronization(selenium, live_server_path, profile_foo)
        transaction_foo_external.refresh_from_db()
        assert transaction_foo_external.external_id is None

    def disable_external_synchronization(
        self,
        selenium: WebDriver,
        live_server_path: Callable[[str], str],
        profile: Profile,
    ) -> None:
        url = live_server_path(reverse("profile_disconnect"))
        selenium.get(url)
        selenium.find_element_by_xpath('//input[@value="Submit"]').click()
        profile.refresh_from_db()
