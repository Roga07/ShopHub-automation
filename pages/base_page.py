from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url: str):
        self.driver.get(url)

    def wait_for_invisibility(self, locator):
        """Espera a que un elemento desaparezca (overlay, loader, etc)"""
        self.wait.until(ec.invisibility_of_element_located(locator))

    def click(self, locator: tuple[str, str]):
        """Espera y hace clic en un elemento."""
        self.driver.find_element(*locator).click()

    def type(self, locator: tuple[str, str], text: str):
        """Espera, limpia y escribe en un input."""
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)

    def text_of_element(self, locator: tuple[str, str]):
        """Devuelve el texto del elemento."""
        return self.driver.find_element(*locator).text