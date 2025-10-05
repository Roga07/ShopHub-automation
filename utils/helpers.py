from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



# Helper para convertir None a cadena vacía
def safe_text(value):
    return "" if value is None else value
