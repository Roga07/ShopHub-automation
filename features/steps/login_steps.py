from behave import given, when, then
from pages.signup_page import SignUp
from pages.login_page import LoginPage


@given('que el usuario está en la página principal')
def step_go_home(context):
    context.signup_page = SignUp(context.driver)
    context.signup_page.load()



@when('el usuario navega a la página de inicio de sesión')
def step_go_to_login(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.go_login()


@when('el usuario ingresa credenciales válidas')
def step_fill_valid(context):
    data = context.table[0]
    context.login_page.login_as_user(email=data['email'],password=data['password'])



@when('el usuario hace clic en el botón de iniciar sesión')
def step_impl(context):
    context.login_page.click_login_button()


@then('el usuario debería ser redirigido al panel principal')
def step_impl(context):
    assert context.login_page.is_dashboard_visible(), "El panel principal no se mostró tras iniciar sesión."


@then('se debería mostrar un mensaje de bienvenida')
def step_impl(context):
    message = context.login_page.get_welcome_message()
    assert "Bienvenido" in message, f"Mensaje de bienvenida no encontrado. Obtenido: {message}"
