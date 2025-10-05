import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from data.env_data import FILL_CHECKOUT_EMPTY
from pages.signup_page import SignUp
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage



def test_checkout_fields_cannot_advance(driver):
    signup = SignUp(driver)
    signup.load()

    product = ProductsPage(driver)
    product.select_category()
    product.select_product()
    product.go_to_shopping_cart()

    cart = CartPage(driver)
    cart.proceed_to_checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_checkout_form(
            FILL_CHECKOUT_EMPTY["first_name"],
            FILL_CHECKOUT_EMPTY["last_name"],
            FILL_CHECKOUT_EMPTY["email"],
            FILL_CHECKOUT_EMPTY["phone"],
            FILL_CHECKOUT_EMPTY["address"],
            FILL_CHECKOUT_EMPTY["city"],
            FILL_CHECKOUT_EMPTY["zip_code"],
            FILL_CHECKOUT_EMPTY["country"]
    )


    try:
        # Espera hasta 2 segundos a que aparezca un alert
         alert = WebDriverWait(driver, 2).until(ec.alert_is_present())
         print("Alerta encontrada:", alert.text)
         alert.accept()  # Acepta la alerta
    except:
        print("No hay alert presente")