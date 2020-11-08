from typing import Callable, Iterable

import pytest
from budget.models import Account, Connection, Transaction
from django.core import mail
from django.shortcuts import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from saltedge_wrapper.factory import customers_api
from selenium.webdriver.firefox.webdriver import WebDriver
from swagger_client.rest import ApiException
from users.models import Profile, User
from users.services import create_customer_in_saltedge
from users.tokens import user_tokenizer

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

    def test_password_reset_link_is_available(
        self, selenium: WebDriver, live_server_path: Callable[[str], str],
    ) -> None:
        url = live_server_path(reverse("login"))
        selenium.get(url)
        element = selenium.find_element_by_link_text("Forgot password?")
        assert element.get_attribute("href") == live_server_path(
            reverse("password_reset")
        )

    def test_invalid_credentials_prints_error_message(
        self, selenium: WebDriver, live_server_path: Callable[[str], str]
    ) -> None:
        url = live_server_path(reverse("login"))
        selenium.get(url)
        self.login_user(selenium, "bar", "xyz")
        messages = [
            m.text
            for m in selenium.find_elements_by_xpath('//div[contains(@class, "alert")]')
        ]
        assert any(
            "Please enter a correct username and password." in message
            for message in messages
        )

    def test_inactive_user_cant_log_in(
        self,
        selenium: WebDriver,
        live_server_path: Callable[[str], str],
        user_foo: User,
    ) -> None:
        user_foo.is_active = False
        user_foo.save()

        url = live_server_path(reverse("login"))
        selenium.get(url)
        self.login_user(selenium, "foo", "password")
        assert selenium.find_elements_by_xpath('//div[contains(@class, "alert")]')
        # Can't check if user is inactive or credentials are wrong - https://code.djangoproject.com/ticket/28645

    def test_next_redirects_to_requested_url(
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
        selenium.find_element_by_xpath('//button[@type="submit"]').click()


class TestSignUp:
    def test_sign_up_redirects_to_login_page(
        self, selenium: WebDriver, live_server_path: Callable[[str], str]
    ) -> None:
        url = live_server_path(reverse("signup"))
        selenium.get(url)
        self.sign_up_user(selenium, "foo", "Foo Password", "foo@example.com")
        assert selenium.current_url == live_server_path(reverse("login"))

    def test_message(
        self, selenium: WebDriver, live_server_path: Callable[[str], str]
    ) -> None:
        url = live_server_path(reverse("signup"))
        selenium.get(url)
        self.sign_up_user(selenium, "foo", "Foo Password", "foo@example.com")
        messages = [
            m.text
            for m in selenium.find_elements_by_xpath('//div[contains(@class, "alert")]')
        ]
        assert any(
            "Please check your inbox for activation link." in message
            for message in messages
        )

    def test_user_with_existing_username_cant_sign_up(
        self,
        selenium: WebDriver,
        live_server_path: Callable[[str], str],
        user_foo: User,
    ) -> None:
        url = live_server_path(reverse("signup"))
        selenium.get(url)
        self.sign_up_user(selenium, "foo", "password", "foo@example.com")
        assert (
            selenium.find_element_by_class_name("invalid-feedback").text
            == "A user with that username already exists."
        )

    def test_sign_up_sends_activation_email(
        self, selenium: WebDriver, live_server_path: Callable[[str], str]
    ) -> None:
        url = live_server_path(reverse("signup"))
        selenium.get(url)
        self.sign_up_user(selenium, "foo", "Foo Password", "foo@example.com")
        assert mail.outbox
        activation_email = mail.outbox[0]
        assert "foo@example.com" in activation_email.to
        assert activation_email.subject == "Budget Supervisor Email Confirmation"
        assert (
            "Please click the following link to complete your registration."
            in activation_email.body
        )

    def test_sign_up_creates_inactive_user(
        self, selenium: WebDriver, live_server_path: Callable[[str], str]
    ) -> None:
        url = live_server_path(reverse("signup"))
        selenium.get(url)
        self.sign_up_user(selenium, "foo", "Foo Password", "foo@example.com")
        user = User.objects.get(username="foo")
        assert user.is_active is False

    def sign_up_user(
        self, selenium: WebDriver, username: str, password: str, email: str
    ) -> None:
        username_input = selenium.find_element_by_name("username")
        username_input.send_keys(username)
        email_input = selenium.find_element_by_name("email")
        email_input.send_keys(email)
        password1_input = selenium.find_element_by_name("password1")
        password1_input.send_keys(password)
        password2_input = selenium.find_element_by_name("password2")
        password2_input.send_keys(password)
        selenium.find_element_by_xpath('//button[@type="submit"]').click()


class TestUserActivateView:
    def test_user_is_activated(
        self,
        selenium: WebDriver,
        live_server_path: Callable[[str], str],
        user_foo_inactive: User,
    ) -> None:
        self.activate_user(selenium, live_server_path, user_foo_inactive)
        assert user_foo_inactive.is_active is True

    def test_redirect(
        self,
        selenium: WebDriver,
        live_server_path: Callable[[str], str],
        user_foo_inactive: User,
    ) -> None:
        self.activate_user(selenium, live_server_path, user_foo_inactive)
        assert selenium.current_url == live_server_path(reverse("login"))

    def test_message(
        self,
        selenium: WebDriver,
        live_server_path: Callable[[str], str],
        user_foo_inactive: User,
    ) -> None:
        self.activate_user(selenium, live_server_path, user_foo_inactive)
        messages = [
            m.text
            for m in selenium.find_elements_by_xpath('//div[contains(@class, "alert")]')
        ]
        assert any(
            "Registration complete. Please login." in message for message in messages
        )

    def test_invalid_user_id(
        self,
        selenium: WebDriver,
        live_server_path: Callable[[str], str],
        user_foo_inactive: User,
    ) -> None:
        user_id = urlsafe_base64_encode(force_bytes(123))
        token = user_tokenizer.make_token(user_foo_inactive)
        url = live_server_path(
            reverse("activate", kwargs={"user_id": user_id, "token": token})
        )
        selenium.get(url)
        messages = [
            m.text
            for m in selenium.find_elements_by_xpath('//div[contains(@class, "alert")]')
        ]
        assert any(
            "Registration confirmation error. Please click the reset password to generate a new confirmation email."
            in message
            for message in messages
        )

    def test_invalid_token(
        self,
        selenium: WebDriver,
        live_server_path: Callable[[str], str],
        user_foo_inactive: User,
    ) -> None:
        user_id = urlsafe_base64_encode(force_bytes(user_foo_inactive.id))
        token = "123"
        url = live_server_path(
            reverse("activate", kwargs={"user_id": user_id, "token": token})
        )
        selenium.get(url)
        messages = [
            m.text
            for m in selenium.find_elements_by_xpath('//div[contains(@class, "alert")]')
        ]
        assert any(
            "Registration confirmation error. Please click the reset password to generate a new confirmation email."
            in message
            for message in messages
        )

    def activate_user(
        self, selenium: WebDriver, live_server_path: Callable[[str], str], user: User
    ) -> None:
        user_id = urlsafe_base64_encode(force_bytes(user.id))
        token = user_tokenizer.make_token(user)
        url = live_server_path(
            reverse("activate", kwargs={"user_id": user_id, "token": token})
        )
        selenium.get(url)
        user.refresh_from_db()


class TestPasswordResetView:
    def test_email(
        self,
        selenium: WebDriver,
        live_server_path: Callable[[str], str],
        user_foo: User,
    ) -> None:
        self.reset_password(selenium, live_server_path, user_foo.email)
        assert mail.outbox
        password_reset_email = mail.outbox[0]
        assert user_foo.email in password_reset_email.to
        assert password_reset_email.subject == "Budget Supervisor Password Reset"
        assert (
            "Please click the following link to reset your password."
            in password_reset_email.body
        )

    def test_redirect(
        self,
        selenium: WebDriver,
        live_server_path: Callable[[str], str],
        user_foo: User,
    ) -> None:
        self.reset_password(selenium, live_server_path, user_foo.email)
        assert selenium.current_url == live_server_path(reverse("login"))

    def reset_password(
        self, selenium: WebDriver, live_server_path: Callable[[str], str], email: str
    ) -> None:
        url = live_server_path(reverse("password_reset"))
        selenium.get(url)
        email_input = selenium.find_element_by_name("email")
        email_input.send_keys(email)
        selenium.find_element_by_xpath('//button[@type="submit"]').click()


class TestPasswordResetConfirmationView:
    def test_password_is_changed(
        self,
        selenium: WebDriver,
        live_server_path: Callable[[str], str],
        user_foo: User,
    ) -> None:
        old_password = user_foo.password
        self.reset_password(selenium, live_server_path, user_foo, "New Password")
        user_foo.refresh_from_db()
        assert user_foo.password != old_password

    def test_redirect(
        self,
        selenium: WebDriver,
        live_server_path: Callable[[str], str],
        user_foo: User,
    ) -> None:
        self.reset_password(selenium, live_server_path, user_foo, "New Password")
        assert selenium.current_url == live_server_path(reverse("budget_index"))

    def reset_password(
        self,
        selenium: WebDriver,
        live_server_path: Callable[[str], str],
        user: User,
        password: str,
    ) -> None:
        user_id = urlsafe_base64_encode(force_bytes(user.id))
        token = user_tokenizer.make_token(user)
        url = live_server_path(
            reverse(
                "password_reset_confirm", kwargs={"uidb64": user_id, "token": token}
            )
        )
        selenium.get(url)
        new_password1_input = selenium.find_element_by_name("new_password1")
        new_password1_input.send_keys(password)
        new_password2_input = selenium.find_element_by_name("new_password2")
        new_password2_input.send_keys(password)
        selenium.find_element_by_xpath('//button[@type="submit"]').click()
        print(selenium.page_source)


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
            for m in selenium.find_elements_by_xpath('//div[contains(@class, "alert")]')
        ]
        assert any(
            "Profile was updated successfully" in message for message in messages
        )

    def update_profile(
        self,
        selenium: WebDriver,
        live_server_path: Callable[[str], str],
        profile: Profile,
    ) -> None:
        url = live_server_path(reverse("profile"))
        selenium.get(url)
        element = selenium.find_element_by_xpath('//button[@type="submit"]')
        element.click()
        profile.refresh_from_db()

    def test_profile_can_be_deleted(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        profile_foo: Profile,
    ) -> None:
        selenium = authenticate_selenium(user=profile_foo.user)
        url = live_server_path(reverse("profile"))
        selenium.get(url)
        element = selenium.find_element_by_link_text("Delete account")
        assert element
        assert element.get_attribute("href") == live_server_path(reverse("user_delete"))

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
            for m in selenium.find_elements_by_xpath('//div[contains(@class, "alert")]')
        ]
        assert any(
            "Profile was connected successfully" in message for message in messages
        )

    def enable_external_synchronization(
        self,
        selenium: WebDriver,
        live_server_path: Callable[[str], str],
        profile: Profile,
    ) -> None:
        url = live_server_path(reverse("profile_connect"))
        selenium.get(url)
        selenium.find_element_by_xpath('//button[@type="submit"]').click()
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
        create_customer_in_saltedge(profile_foo, customers_api())
        self.disable_external_synchronization(selenium, live_server_path, profile_foo)
        assert profile_foo.external_id is None

    def test_customer_is_deleted(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        profile_foo: Profile,
        remove_temporary_customers: Callable[[], Iterable[None]],
    ) -> None:
        api = customers_api()
        create_customer_in_saltedge(profile_foo, api)
        external_id = profile_foo.external_id
        selenium = authenticate_selenium(user=profile_foo.user)
        assert api.customers_customer_id_get(external_id)
        self.disable_external_synchronization(selenium, live_server_path, profile_foo)
        with pytest.raises(ApiException) as e:
            api.customers_customer_id_get(external_id)
        assert "CustomerNotFound" in str(e.value)

    def test_redirect(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        profile_foo: Profile,
        remove_temporary_customers: Callable[[], Iterable[None]],
    ) -> None:
        selenium = authenticate_selenium(user=profile_foo.user)
        create_customer_in_saltedge(profile_foo, customers_api())
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
        create_customer_in_saltedge(profile_foo, customers_api())
        self.disable_external_synchronization(selenium, live_server_path, profile_foo)
        messages = [
            m.text
            for m in selenium.find_elements_by_xpath('//div[contains(@class, "alert")]')
        ]
        assert any(
            "Profile was disconnected successfully" in message for message in messages
        )

    def test_connections_deleted(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        profile_foo: Profile,
        connection_foo: Connection,
        remove_temporary_customers: Callable[[], Iterable[None]],
    ) -> None:
        selenium = authenticate_selenium(user=profile_foo.user)
        create_customer_in_saltedge(profile_foo, customers_api())
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
        create_customer_in_saltedge(profile_foo, customers_api())
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
        create_customer_in_saltedge(profile_foo, customers_api())
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
        selenium.find_element_by_xpath('//button[@type="submit"]').click()
        profile.refresh_from_db()


class TestUserDelete:
    def test_user_is_deleted(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.delete_user(selenium, live_server_path, user_foo)
        assert not User.objects.filter(pk=user_foo.pk).exists()

    def test_profile_is_deleted(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.delete_user(selenium, live_server_path, user_foo)
        assert not Profile.objects.filter(pk=user_foo.profile.pk).exists()

    def test_redirect(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.delete_user(selenium, live_server_path, user_foo)
        assert selenium.current_url == live_server_path(reverse("login"))

    def test_message(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.delete_user(selenium, live_server_path, user_foo)
        messages = [
            m.text
            for m in selenium.find_elements_by_xpath('//div[contains(@class, "alert")]')
        ]
        assert any("User was deleted successfully" in message for message in messages)

    def test_connections_are_deleted(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        connection_foo: Connection,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.delete_user(selenium, live_server_path, user_foo)
        assert not Connection.objects.filter(user=user_foo).count() == 0

    def test_accounts_are_deleted(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        account_foo: Account,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.delete_user(selenium, live_server_path, user_foo)
        assert not Account.objects.filter(user=user_foo).count() == 0

    def test_transactions_are_deleted(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        transaction_foo: Transaction,
    ) -> None:
        selenium = authenticate_selenium(user=user_foo)
        self.delete_user(selenium, live_server_path, user_foo)
        assert not Transaction.objects.filter(user=user_foo).count() == 0

    def test_customer_is_deleted(
        self,
        authenticate_selenium: Callable[..., WebDriver],
        live_server_path: Callable[[str], str],
        user_foo: User,
        remove_temporary_customers: Callable[[], Iterable[None]],
    ) -> None:
        api = customers_api()
        create_customer_in_saltedge(user_foo.profile, api)
        selenium = authenticate_selenium(user=user_foo)
        assert api.customers_customer_id_get(user_foo.profile.external_id)
        self.delete_user(selenium, live_server_path, user_foo)
        with pytest.raises(ApiException) as e:
            api.customers_customer_id_get(user_foo.profile.external_id)
        assert "CustomerNotFound" in str(e.value)

    def delete_user(
        self, selenium: WebDriver, live_server_path: Callable[[str], str], user: User,
    ) -> None:
        url = live_server_path(reverse("user_delete"))
        selenium.get(url)
        selenium.find_element_by_xpath('//button[@type="submit"]').click()
