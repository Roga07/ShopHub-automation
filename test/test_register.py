import pytest
from data.env_data import SIGNUP_INVALID_FORMAT_EMAIL
from pages.signup_page import SignUp


@pytest.mark.signup
def test_invalid_format_email(driver):
    signup = SignUp(driver)
    signup.load()
    signup.sign_up()
    signup.signup_as_user(
        SIGNUP_INVALID_FORMAT_EMAIL["first_name"],
        SIGNUP_INVALID_FORMAT_EMAIL["last_name"],
        SIGNUP_INVALID_FORMAT_EMAIL["email"],
        SIGNUP_INVALID_FORMAT_EMAIL["zip_code"],
        SIGNUP_INVALID_FORMAT_EMAIL["password"]
    )

    signup.assert_signup_campos()
