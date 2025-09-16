from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

  #Espera a que un elemento desaparezca (loader,overlay)
    def wait_until_disappears(self,locator):
        self.wait.until(ec.invisibility_of_element_located(locator))

    def open(self, url: str):
        self.driver.get(url)

    def click(self, locator: tuple[By, str]):
        self.driver.find_element(*locator).click()

    def type(self, locator: tuple[By, str], text: str):
        element =self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)


