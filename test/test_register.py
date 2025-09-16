import pytest
from pages.signup_page import SignUp
from selenium.webdriver.support.ui import WebDriverWait



FIRST_NAME = "John"
LAST_NAME = "Doe"
EMAIL = "john.doe@example.com"
ZIP_CODE = "23085"
PASSWORD = "Password123"

EXPECTED_URL = "https://shophub-commerce.vercel.app/signup/success"


@pytest.mark.e2e
def test_user_register(driver):
    signup = SignUp(driver)
    signup.load()
    signup.sign_up()
    signup.signup_as_user(FIRST_NAME,LAST_NAME,EMAIL,ZIP_CODE,PASSWORD)


    #Espera explicitamente a que la pagina de exito cargue
    WebDriverWait(driver,10).until( lambda d: d.current_url == EXPECTED_URL)

    #Assertion usando el link actual
    current_url = driver.current_url
    assert current_url == EXPECTED_URL