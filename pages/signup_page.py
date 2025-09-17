from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SignUp(BasePage):
    """
    Clase Page Object para la página de registro (Sign Up) de Shophub.

    Hereda de BasePage para reutilizar métodos genéricos de Selenium
    como click, type, open y wait_until_disappears.
    """

    # URL de la página principal
    URL = "https://shophub-commerce.vercel.app"

    # Selectores de los elementos de la página
    SIGNUP_BUTTON = (By.CSS_SELECTOR, "a[href='/signup']")  # Botón para abrir el formulario de registro
    OVERLAY = (By.CSS_SELECTOR, "div.fixed.inset-0.z-50")   # Overlay que bloquea la interacción mientras carga
    BUTTON_SIGNUP = (By.XPATH, "//button[@type='submit' and normalize-space(.)='Sign Up']")  # Botón para enviar el formulario

    FIRST_NAME = (By.ID, "firstName")  # Campo de nombre
    LAST_NAME = (By.ID, "lastName")    # Campo de apellido
    EMAIL = (By.ID, "email")           # Campo de correo electrónico
    ZIP_CODE = (By.ID, "zipCode")      # Campo de código postal
    INPUT_PASSWORD = (By.ID, "password")  # Campo de contraseña

    # -----------------------
    # Métodos de interacción
    # -----------------------

    def load(self):
        """
        Abre la página principal de la aplicación.
        """
        self.open(self.URL)

    def sign_up(self):
        """
        Abre el formulario de registro:
        1. Espera a que el overlay desaparezca.
        2. Hace clic en el botón de 'Sign Up'.
        """
        self.wait_until_disappears(self.OVERLAY)
        self.click(self.SIGNUP_BUTTON)

    def signup_as_user(self, firstname: str, lastname: str, email: str, zipcode: str, password: str):
        """
        Llena el formulario de registro y lo envía.

        Args:
            firstname (str): Nombre del usuario.
            lastname (str): Apellido del usuario.
            email (str): Correo electrónico del usuario.
            zipcode (str): Código postal.
            password (str): Contraseña del usuario.
        """
        self.wait_until_disappears(self.OVERLAY)  # Esperar que desaparezca el overlay
        self.type(self.FIRST_NAME, firstname)     # Escribir el nombre
        self.type(self.LAST_NAME, lastname)       # Escribir el apellido
        self.type(self.EMAIL, email)              # Escribir el email
        self.type(self.ZIP_CODE, zipcode)         # Escribir el código postal
        self.type(self.INPUT_PASSWORD, password)  # Escribir la contraseña
        self.click(self.BUTTON_SIGNUP)            # Enviar el formulario

    def assert_signup_title(self):
        """
        Verifica que el registro fue exitoso.
        Comprueba que el título de la página contenga 'Signup Successful'.
        """
        self.wait_until_disappears(self.OVERLAY)
        assert "Signup Successful" in self.driver.title, "El título de la página no indica éxito en el registro"



