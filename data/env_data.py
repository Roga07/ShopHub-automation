import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By


load_dotenv() #carga las variables del .env

# Detectar si estamos en CI (GitHub Actions, etc.)
CI_ENV = os.getenv("CI", "false").lower() == "true"


# URL de la página principal
BASE_URL = "https://shophub-commerce.vercel.app"
#OVERLAY
OVERLAY = (By.CSS_SELECTOR, "div.fixed.inset-0.z-50.flex.items-center.justify-center.bg-background\\/70")

SIGNUP_USER = {
    "first_name": os.getenv("FIRST_NAME"),
    "last_name": os.getenv("LAST_NAME"),
    "email": os.getenv("EMAIL"),
    "zip_code": os.getenv("ZIP_CODE"),
    "password": os.getenv("PASSWORD")
}

for key, value in SIGNUP_USER.items():
    if not value:
        raise ValueError(f"{key} no puede ser None o vacío")

CUSTOMER_INFORMATION = {
    "first_name": os.getenv("FIRST_NAME"),
    "last_name": os.getenv("LAST_NAME"),
    "email": os.getenv("EMAIL"),
    "phone": os.getenv("PHONE"),
    "address": os.getenv("ADDRESS"),
    "city": os.getenv("CITY"),
    "zip_code": os.getenv("ZIP_CODE"),
    "country": os.getenv("COUNTRY")

}

SIGNUP_INVALID_FORMAT_EMAIL= {
    "first_name": os.getenv("FIRST_NAME_FAIL"),
    "last_name": os.getenv("LAST_NAME_FAIL"),
    "email": os.getenv("EMAIL_FAIL"),
    "zip_code": os.getenv("ZIP_CODE_FAIL"),
    "password": os.getenv("PASSWORD_FAIL")

}

LOGIN_UNREGISTERED_USER = {
    "email": os.getenv("EMAIL_UNREGISTERED"),
    "password": os.getenv("PASSWORD_UNREGISTERED")
}

# === Diccionario de prueba con campos vacíos ===
FILL_CHECKOUT_EMPTY = {
    "first_name": " ",
    "last_name": " ",
    "email": " ",
    "phone": " ",
    "address": " ",
    "city": " ",
    "zip_code": " ",
    "country": " "
}

# === Validación de variables importantes ===
# Solo validar si NO estamos en CI
if not CI_ENV:
    for key, value in SIGNUP_USER.items():
        if not value or value.strip() == "":
            raise ValueError(f"{key} no puede ser None o vacío")

# === Opcional: imprimir para debug local ===
if not CI_ENV:
    print("✅ Variables cargadas correctamente:", SIGNUP_USER)
