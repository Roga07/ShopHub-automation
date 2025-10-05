from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from data.env_data import OVERLAY



class ProductsPage(BasePage):

    #Selectores de elementos

    SELECT_ELECTRONICS = (By.CSS_SELECTOR,"img[alt='Electronics']")
    SELECT_WIRELESS = (By.XPATH,"//*[@id='add-to-cart-23']")
    SELECT_SMART = (By.XPATH,"//*[@id='add-to-cart-24']")
    CART_LINK = (By.CSS_SELECTOR, "a[href='/cart']")
    VIEW_DETAILS_WIRELESS = (By.ID,"view-details-23")

    PRODUCT_NOT_FOUND_TITLE = (By.TAG_NAME, "h2")
    ERROR_MESSAGE = (By.ID, "product-404-message")

    def select_category(self):
        self.wait_for_invisibility(OVERLAY)
        self.click(self.SELECT_ELECTRONICS)

    def select_product(self):
        self.wait_for_invisibility(OVERLAY)
        self.click(self.SELECT_WIRELESS)
        self.click(self.SELECT_SMART)

    def go_to_shopping_cart(self):
        self.click(self.CART_LINK)

    def details_product(self):
        self.wait_for_invisibility(OVERLAY)
        self.click(self.VIEW_DETAILS_WIRELESS)

    def assert_product_not_found(self):
        """Verifica que el mensaje de 'Producto No Encontrado' es visible."""
        self.wait_for_invisibility(OVERLAY)

        # Intenta obtener el texto del título de error (usando h2 como ejemplo)
        error_text = self.text_of_element(self.PRODUCT_NOT_FOUND_TITLE)

        # La aserción clave: El texto debe contener el mensaje de error esperado.
        assert "Product Not Found" in error_text or "404" in error_text, \
            f"Esperaba 'Product Not Found', pero encontré: '{error_text}'"

        return error_text
    



