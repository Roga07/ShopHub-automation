from selenium.webdriver.common.by import By
from conftest import driver
from pages.base_page import BasePage
from data.env_data import OVERLAY


class CheckoutCompletePage(BasePage):



    def validate_purchase_completion_url(self):
        self.wait_for_invisibility(OVERLAY)
        assert self.driver.current_url == "https://shophub-commerce.vercel.app/confirmation"
        #print(">>> Current URL:", self.driver.current_url)