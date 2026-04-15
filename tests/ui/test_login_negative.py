from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_lockedout_user(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login_credentials_visible()
    login_page.type_username("locked_out_user")
    login_page.type_password("secret_sauce")
    login_page.click_login()
    login_page.expect_error_msg("Epic sadface: Sorry, this user has been locked out.")

def test_invalid_user(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login_credentials_visible()
    login_page.type_username("invalid_user")
    login_page.type_password("secret_pswd")
    login_page.click_login()
    login_page.expect_error_msg("Epic sadface: Username and password do not match any user in this service")

def test_invalid_password(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login_credentials_visible()
    login_page.type_username("performance_glitch_user")
    login_page.type_password("bad_pswd")
    login_page.click_login()
    login_page.expect_error_msg("Epic sadface: Username and password do not match any user in this service")

def test_empty_user(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login_credentials_visible()
    login_page.type_username("")
    login_page.type_password("secret_pswd")
    login_page.click_login()
    login_page.expect_error_msg("Epic sadface: Username is required")

def test_empty_password(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login_credentials_visible()
    login_page.type_username("user")
    login_page.type_password()
    login_page.click_login()
    login_page.expect_error_msg("Epic sadface: Password is required")