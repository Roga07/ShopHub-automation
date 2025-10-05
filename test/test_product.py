import pytest
from pages.signup_page import SignUp
from pages.products_page import ProductsPage


EXPECTED_ERROR = "Product Not Found"

@pytest.mark.product
def test_product_details(driver):

    signup = SignUp(driver)
    signup.load()

    product = ProductsPage(driver)
    product.select_category()
    product.details_product()

    # 3. La aserción: Verificar que el error esperado SÍ aparece
    print(f"Verificando que aparece el mensaje: '{EXPECTED_ERROR}'")
    product.assert_product_not_found()
    print("Test Negativo Exitoso: El error 'Product Not Found' fue validado.")

