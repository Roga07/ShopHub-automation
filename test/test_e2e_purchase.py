import pytest
from data.env_data import SIGNUP_USER, CUSTOMER_INFORMATION
from pages.signup_page import SignUp
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.chekout_complete_page import CheckoutCompletePage

@pytest.mark.e2e
def test_user_register1(driver):
    signup = SignUp(driver)
    signup.load()
    signup.sign_up()
    signup.signup_as_user(
        SIGNUP_USER["first_name"],
        SIGNUP_USER["last_name"],
        SIGNUP_USER["email"],
        SIGNUP_USER["zip_code"],
        SIGNUP_USER["password"]
    )
    signup.click_go_home()


    login = LoginPage(driver)
    login.go_login()
    login.login_as_user(SIGNUP_USER["email"],SIGNUP_USER["password"])
    login.click_go_home()

    product = ProductsPage(driver)
    product.select_category()
    product.select_product()
    product.go_to_shopping_cart()

    cart = CartPage(driver)
    cart.proceed_to_checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_checkout_form(
        CUSTOMER_INFORMATION["first_name"],
        CUSTOMER_INFORMATION["last_name"],
        CUSTOMER_INFORMATION["email"],
        CUSTOMER_INFORMATION["phone"],
        CUSTOMER_INFORMATION["address"],
        CUSTOMER_INFORMATION["city"],
        CUSTOMER_INFORMATION["zip_code"],
        CUSTOMER_INFORMATION["country"]
    )

    checkout_complete = CheckoutCompletePage(driver)
    checkout_complete.validate_purchase_completion_url()