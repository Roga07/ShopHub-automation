from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from data.env_data import OVERLAY



class CartPage(BasePage):

    #Selectopres

    BUTTON_CHECKOUT = (By.XPATH,"//button[normalize-space()='Proceed to Checkout']")
    BUTTON_CONTINUE_SHOPPING = (By.XPATH,"//button[normalize-space()='Continue Shopping']")


    def proceed_to_checkout(self):
        self.wait_for_invisibility(OVERLAY)
        self.click(self.BUTTON_CHECKOUT)

    def continue_shopping(self):
        self.wait_for_invisibility(OVERLAY)
        self.click(self.BUTTON_CONTINUE_SHOPPING)

