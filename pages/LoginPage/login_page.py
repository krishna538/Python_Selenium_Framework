from base.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    def __init__(self,driver):
        super(LoginPage, self).__init__(driver)
        self.driver = driver

    # login page locators
    _username_field = "txtUsername"
    _password_field = "txtPassword"
    _login_button = "btnLogin"

    def enterUserName(self, username):
        element = self.driver.find_element(By.ID, self._username_field)
        element.send_keys(username)

    def enterPassword(self, password):
        element = self.driver.find_element(By.ID, self._password_field)
        element.send_keys(password)

    def clickOnLoginButton(self):
        element = self.driver.find_element(By.ID, self._login_button)
        element.click()

    def login(self, username, password):
        self.enterUserName(username)
        self.enterPassword(password)
        self.clickOnLoginButton()



