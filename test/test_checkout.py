import pytest
from data.env_data import SIGNUP_USER, FILL_CHECKOUT_EMPTY
from pages.signup_page import SignUp
from pages.checkout_page import CheckoutPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.chekout_complete_page import CheckoutCompletePage




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

    checkout_complete = CheckoutCompletePage(driver)
    checkout_complete.validate_purchase_completion_url()

