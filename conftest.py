import pytest
from utils.driver_factory import create_driver
from time import sleep

#Define los Fixture que se comparten con pytest
def pytest_addoption(parser):
     parser.addoption(
        "--headless",
        action="store_true", #alamcene datos
        help="Ejecutar pruebas en modo headless (sin interfaz de usuario)"
    )


@pytest.fixture
def driver(request):     #genera y return un driver
    headless = request.config.getoption("--headless")
    driver = create_driver(headless=headless)
    yield driver
    sleep(3)
    driver.quit()