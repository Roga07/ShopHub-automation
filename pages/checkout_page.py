from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from data.env_data import OVERLAY



class CheckoutPage(BasePage):


    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "email")
    PHONE = (By.ID,"phone")
    ADDRESS = (By.ID,"address")
    CITY = (By.ID, "city")
    ZIP_CODE = (By.ID, "zipCode")
    COUNTRY = (By.ID, "country")
    BUTTON_ORDER = (By.ID,"place-order-button")

    def fill_checkout_form(self, firstname: str, lastname: str, email: str, phone:str, address:str, city: str, zipcode: str, country: str):
        self.type(self.FIRST_NAME, firstname)
        self.type(self.LAST_NAME, lastname)
        self.type(self.EMAIL, email)
        self.type(self.PHONE, phone)
        self.type(self.ADDRESS,address)
        self.type(self.CITY, city)
        self.type(self.ZIP_CODE, zipcode)
        self.type(self.COUNTRY, country)
        self.wait_for_invisibility(OVERLAY)
        self.click(self.BUTTON_ORDER)