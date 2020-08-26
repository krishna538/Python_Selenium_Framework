import pytest
from pages.LoginPage.login_page import LoginPage
import unittest


@pytest.mark.usefixtures("setUp")
class test_LoginPageTests(unittest.TestCase):
    lp = None

    @pytest.fixture(autouse=True)
    def classSetup(self, setUp):
        self.lp = LoginPage(setUp)

    def test_valid_login(self):
        self.lp.login("Admin", "admin123")

    def test_invalid_login(self):
        self.lp.login("Admin", "admin111")

