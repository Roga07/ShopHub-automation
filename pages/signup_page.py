from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from data.env_data import BASE_URL,OVERLAY
from selenium.webdriver.support import expected_conditions as EC


class SignUp(BasePage):
    # Selectores de la página principal
    SIGNUP_HOME = (By.CSS_SELECTOR, "a[href='/signup']")
    GO_HOME = (By.CSS_SELECTOR, "a[href='/']")

    # Selectores del formulario
    BUTTON_SIGNUP = (By.XPATH, "//button[@type='submit' and normalize-space(.)='Sign Up']")
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "email")
    ZIP_CODE = (By.ID, "zipCode")
    INPUT_PASSWORD = (By.ID, "password")

    SUCCESS_TITLE = (By.TAG_NAME, "h1")

    # --------------------
    # Acciones
    # --------------------
    def load(self):
        self.open(BASE_URL)

    def sign_up(self):
        self.wait_for_invisibility(OVERLAY)
        """Clic en el enlace de signup desde home."""
        self.click(self.SIGNUP_HOME)


    def signup_as_user(self, firstname: str, lastname: str, email: str, zipcode: str, password: str):
        """Llena el formulario y envía."""

       # self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME))

        self.type(self.FIRST_NAME, firstname)
        self.type(self.LAST_NAME, lastname)
        self.type(self.EMAIL, email)
        self.type(self.ZIP_CODE, zipcode)
        self.type(self.INPUT_PASSWORD, password)
        self.wait_for_invisibility(OVERLAY)
        self.click(self.BUTTON_SIGNUP)
       # self.wait.until(EC.presence_of_element_located(self.SUCCESS_TITLE))


    def click_go_home(self):
        self.wait_for_invisibility(OVERLAY)
        """Clic en el botón o enlace para regresar al home."""
        self.click(self.GO_HOME)

    def assert_signup_title(self):
        self.wait_for_invisibility(OVERLAY)
        assert "Signup Successful" in self.driver.find_element(By.TAG_NAME, "h1").text

    def assert_signup_campos(self):
        email_input = self.driver.find_element(*self.EMAIL)
        validation_msg = self.driver.execute_script(
            "return arguments[0].validationMessage;", email_input
        )
        assert validation_msg != "", f"El campo email no mostró mensaje de validación: {validation_msg}"
        print(validation_msg)




