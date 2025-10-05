from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

#Crea y configura el WebDriver

def create_driver(headless: bool = False):
    options = webdriver.ChromeOptions()

    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--windows-size=1080, 720")
        options.add_argument("--incognito")

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), #Para que lo install por mi
        options=options
    )

    driver.implicitly_wait(5) #Instanciamos
    return driver