from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from data.env_data import OVERLAY
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



class LoginPage(BasePage):

    #Selectores de los elementos

    BUTTON_LOGIN_HOME = (By.XPATH,"//button[contains(text(),'Login')]")
    EMAIL_LOGIN = (By.ID,"email")
    PASSWORD_LOGIN = (By.ID,"password")
    BUTTON_LOGIN = (By.CSS_SELECTOR,"button[type='submit']")

    GO_HOME = (By.CSS_SELECTOR, "a[href='/']")


    def go_login(self):
        self.wait_for_invisibility(OVERLAY)
        self.click(self.BUTTON_LOGIN_HOME)

    def login_as_user(self, email: str, password: str):
        self.wait_for_invisibility(OVERLAY)
        self.type(self.EMAIL_LOGIN, email)
        self.type(self.PASSWORD_LOGIN, password)
        self.click(self.BUTTON_LOGIN)

    def click_go_home(self):
        self.wait_for_invisibility(OVERLAY)
        """Clic en el botón o enlace para regresar al home."""
        self.click(self.GO_HOME)


    def assert_login_title(self):
        self.wait_for_invisibility(OVERLAY)
        assert "Logged In" in self.driver.find_element(By.TAG_NAME, "h1").text

    def assert_login_failed(self):
        self.wait_for_invisibility(OVERLAY)
        current_title = self.driver.find_element(By.TAG_NAME, "h1").text
        return current_title


