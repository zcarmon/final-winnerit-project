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
        self.__page.goto(url)

    def type_username(self, username: str, ddelay = 100):
        self.__username_locator.press_sequentially(username,delay = ddelay)

    def type_password(self, password: str):
        self.__password_locator.fill(password)

    def click_login(self):
        self.__login_button_locator.click()

# # Assertions
    def expect_error_msg(self, error_message: str):
        expect(self.__error_message).to_contain_text(error_message)

    def login_credentials_visible(self):
        expect(self.__login_credential).to_be_visible()