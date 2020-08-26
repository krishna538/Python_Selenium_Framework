import pytest
from base.WebDriverFactory import WebDriverFactory


@pytest.yield_fixture()
def setUp(request, browser):
    print("Running browser setup and launching")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriver()
    print("browser launched successfully")
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("browser is closed successfully")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--platform")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def platform(request):
    return request.config.getoption("--platform")