from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_example1(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login_credentials_visible()
    login_page.type_username("locked_out_user")
    login_page.type_password("secret_sauce")
    login_page.click_login()
    login_page.expect_error_msg("Epic sadface: Sorry, this user has been locked out.")

def test_example2(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    expect(page.locator("[data-test=\"login-credentials\"]")).to_be_visible()

    page.locator("[data-test=\"username\"]").press_sequentially("invalid_user",delay=200)
    page.locator("[data-test=\"password\"]").fill("secret_saucefas")
    page.locator("[data-test=\"login-button\"]").click()
    expect(page.locator("[data-test=\"error\"]")).to_contain_text("Epic sadface: Username and password do not match any user in this service")
