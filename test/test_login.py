import pytest
from data.env_data import LOGIN_UNREGISTERED_USER
from pages.login_page import LoginPage
from pages.signup_page import SignUp

@pytest.mark.xfail(reason="La app no valida usuarios no registrados aún")
def test_unregistered_user(driver):
    login = LoginPage(driver)
    signup = SignUp(driver)
    signup.load()
    login.go_login()
    login.login_as_user(LOGIN_UNREGISTERED_USER["email"], LOGIN_UNREGISTERED_USER["password"])

    # Asumiendo que assert_login_title devuelve el título actual:
    actual_title = login.assert_login_failed()
    assert actual_title != "Logged In", f"El usuario no registrado inició sesión: {actual_title}"

