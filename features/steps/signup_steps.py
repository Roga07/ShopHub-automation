from behave import given, when, then
from selenium import webdriver
from pages.signup_page import SignUp


@given("el usuario esta en la pagina home")
def step_user_on_homepage(context):
    context.driver = webdriver.Chrome()
    context.page = SignUp(context.driver)
    context.page.load() #abre la URL principal

@when("el usuario navega a la pagina de signup")
def step_user_navigates_signup(context):
    context.page.sigup() #hace click en el boton signup

@when("el usuario rellena el formulario de registro con datos validos")
def step_user_fills_form(context):
    context.page.signup_as_user(
        "John",
        "Doe",
        "john.doe@example.com",
        "23085",
        "Password123"
    )

@then("el usuario debe ser redirigido a la pagina de exito")
def step_user_redirected_success(context):
    assert "signup/success" in context.driver.current_url
    context.driver.quit()


