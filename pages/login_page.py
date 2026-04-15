import allure
from playwright.sync_api import Page, expect

class LoginPage:

    def __init__(self, page: Page) -> None:
        self.__page = page
        self.__username_locator = page.locator("[data-test=\"username\"]").describe("Username field")
        self.__password_locator = page.locator("[data-test=\"password\"]").describe("Password field")
        self.__login_button_locator = page.locator("[data-test=\"login-button\"]").describe("Login Button")
        self.__login_credential = page.locator("[data-test=\"login-credentials\"]").describe("Credential field")
        self.__error_message = page.locator("[data-test=\"error\"]").describe("Error message")

# # Methods
    def navigate(self, url = "https://www.saucedemo.com/"):
        with allure.step("Navigate to " + url):
            self.__page.goto(url)

    def type_username(self, username: str, ddelay = 100):
        with allure.step(f"Typing username [{username}]"):
            self.__username_locator.press_sequentially(username,delay = ddelay)

    def type_password(self, password=""):
        with allure.step(f"Typing password [{password}]"):
            self.__password_locator.fill(password)

    def click_login(self):
        with allure.step("Login to saucedemo"):
            self.__login_button_locator.click()

# # Assertions
    def expect_error_msg(self, error_message: str):
        with allure.step(f"Error message [{error_message}]"):
            expect(self.__error_message).to_contain_text(error_message)

    def login_credentials_visible(self):
        with allure.step("Login credentials"):
            expect(self.__login_credential).to_be_visible()