from selenium import webdriver
from pathlib import Path


class WebDriverFactory:

    def __init__(self, browser):
        self.browser = browser

    def getWebDriver(self):
        baseUrl = "https://opensource-demo.orangehrmlive.com/"
        driver = None
        try:
            if self.browser is not None:
                if self.browser == "chrome":
                    driver_path = str(Path(__file__).parent.parent)
                    driver_path = driver_path + '\\drivers\\chromedriver.exe'
                    driver = webdriver.Chrome(executable_path=driver_path)
                elif self.browser == "firefox":
                    pass
                elif self.browser == "ie":
                    pass
                else:
                    print("Requested is not a valid web browser")
            else:
                print("provide the browser name to initiate")
        except:
            print("###### Error occurred")
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)
        return driver

