from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SignUp(BasePage):

    #Pagina
    URL = "https://shophub-commerce.vercel.app"

    #Selectores
    SIGNUP_BUTTON = (By.CSS_SELECTOR,"a[href='/signup']")
    OVERLAY = (By.CSS_SELECTOR, "div.fixed.inset-0.z-50")

    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "email")
    ZIP_CODE = (By.ID,"zipCode")
    INPUT_PASSWORD = (By.ID, "password")
    BUTTON_SIGNUP =  (By.XPATH, "//button[@type='submit' and normalize-space(.)='Sign Up']")



    #Aciones
    def load(self):
        self.open(self.URL)

    def sign_up(self):
        self.wait_until_disappears(self.OVERLAY)
        self.click(self.SIGNUP_BUTTON)


    def signup_as_user(self, firstname: str, lastname: str, email: str, zipcode: str, password: str,):
        self.wait_until_disappears(self.OVERLAY)
        self.type(self.FIRST_NAME, firstname)
        self.type(self.LAST_NAME, lastname)
        self.type(self.EMAIL, email)
        self.type(self.ZIP_CODE, zipcode)
        self.type(self.INPUT_PASSWORD, zipcode)
        self.click(self.BUTTON_SIGNUP)

    def assert_signup_tittle(self):
        self.wait_until_disappears(self.OVERLAY)
        assert "Signup Successful" in self.driver.title


