from behave import given, when, then
from pages.signup_page import SignUp
from selenium.webdriver.support import expected_conditions as EC


@given('que el usuario està en la pagina principal')
def step_go_to_home(context):
    context.signup_page = SignUp(context.driver)
    context.signup_page.load()


@when('el usuario navega a la pagina de registro')
def step_go_to_register(context):
    context.signup_page.sign_up()
    # Espera explícita de seguridad
    context.signup_page.wait.until(EC.presence_of_element_located(context.signup_page.FIRST_NAME))


@when('el usuario completa el formulario de registro con datos vàlidos')
def step_fill_valid_data(context):
    data = context.table[0].as_dict()  # <- importante
    context.signup_page.signup_as_user(
        firstname=data['first_name'],
        lastname=data['last_name'],
        email=data['email'],
        zipcode=data['zip_code'],
        password=data['password']
    )


@when('el usuario envia el formulario')
def step_submit_form(context):
    # ya lo hace dentro de signup_as_user, pero lo dejamos por claridad
    pass


@then('el usuario deberia ser redirigido a la pagina de registro exitoso')
def step_verify_redirect(context):
    context.signup_page.assert_signup_title()


@then('se deberia mostrar un mensaje de confirmacion.')
def step_verify_confirmation(context):
    # Ya se valida dentro de assert_signup_title, así que no hace falta más
    pass


@when('el usuario completa el formulario de registro con datos invàlidos')
def step_fill_invalid_data(context):
    data = context.table[0]
    context.signup_page.signup_as_user(
        firstname=data['first_name'],
        lastname=data['last_name'],
        email=data['email'],
        zipcode=data['zip_code'],
        password=data['password']
    )


@then('se deberia mostrar un mensaje de validacion en el campo email')
def step_verify_invalid_email(context):
    context.signup_page.assert_signup_campos()


