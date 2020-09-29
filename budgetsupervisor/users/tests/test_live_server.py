import pytest
from django.shortcuts import reverse


pytestmark = pytest.mark.selenium


def test_login_success_redirects_to_budget_index(selenium, live_server_path, user_foo):
    url = live_server_path(reverse("login"))
    selenium.get(url)
    username_input = selenium.find_element_by_name("username")
    username_input.send_keys("foo")
    password_input = selenium.find_element_by_name("password")
    password_input.send_keys("password")
    selenium.find_element_by_xpath('//input[@value="login"]').click()
    assert selenium.current_url == live_server_path(reverse("budget_index"))
