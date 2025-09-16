# README.md

# 🧪 Proyecto de Automatización de Pruebas con Selenium + Pytest

[![CI](https://github.com/tu-usuario/tu-repo/actions/workflows/tests.yml/badge.svg)](https://github.com/tu-usuario/tu-repo/actions/workflows/tests.yml)
![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![Pytest](https://img.shields.io/badge/pytest-✓-green.svg)
![Last Commit](https://img.shields.io/github/last-commit/tu-usuario/tu-repo)

Este proyecto implementa pruebas automatizadas utilizando **Selenium WebDriver**, **Pytest** y el patrón **Page Object Model (POM)**.  
Está diseñado para validar el flujo de **registro (Sign Up)** y **login** en la aplicación [ShopHub](https://shophub-commerce.vercel.app/).

---

## 🚀 Tecnologías utilizadas
- [Python 3.11+](https://www.python.org/)
- [Selenium](https://www.selenium.dev/)
- [Pytest](https://docs.pytest.org/)
- [Webdriver Manager](https://github.com/SergeyPirogov/webdriver_manager)
- GitHub Actions (CI/CD)

---

## 📂 Estructura del proyecto
```
.
├── pages/                # Page Objects
│   ├── base_page.py
│   ├── login_page.py
│   ├── signup_page.py
│   └── ...
├── tests/                # Casos de prueba
│   ├── test_login.py
│   ├── test_signup.py
│   └── ...
├── utils/                # Utilidades (driver_factory, config, etc.)
├── requirements.txt      # Dependencias del proyecto
├── README.md             # Este archivo 📘
└── .github/workflows/    # Workflows de CI/CD
```

---

## ⚙️ Instalación y configuración

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/tu-repo.git
   cd tu-repo
   ```

2. Crea un entorno virtual e instala dependencias:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux / Mac
   .venv\Scripts\activate      # Windows
   pip install -r requirements.txt
   ```

3. Ejecuta los tests:
   ```bash
   pytest -v --tb=short
   ```

---

## 🧪 Ejemplo de prueba (Signup)

```python
@pytest.mark.e2e
def test_user_signup(driver):
    signup = SignupPage(driver)
    signup.load()
    signup.signup_as_user("John", "Doe", "john@example.com", "23085", "SuperSecret123")

    # Verificar URL de éxito
    WebDriverWait(driver, 10).until(
        lambda d: d.current_url == "https://shophub-commerce.vercel.app/signup/success"
    )
    assert "success" in driver.current_url
```

---

## 🤖 Integración continua (CI/CD)

Este proyecto incluye un workflow de **GitHub Actions** que corre automáticamente los tests en cada `push` o `pull request`.

Archivo: `.github/workflows/tests.yml`

[![CI](https://github.com/tu-usuario/tu-repo/actions/workflows/tests.yml/badge.svg)](https://github.com/tu-usuario/tu-repo/actions/workflows/tests.yml)

---

## 📸 Screenshots y reportes

Si las pruebas fallan, los screenshots y logs se guardarán en la carpeta `reports/` o como artifacts en GitHub Actions.

---

## ✨ Futuras mejoras
- Agregar pruebas de carrito de compras 🛒  
- Integrar reportes con **Allure**  
- Ejecución en Docker con Selenium Grid  

---

## 👨‍💻 Autor
**Roberto Gamboa López**  
- 💼 QA Automation Tester  
- 🌍 Chiapas, México  
- 📧 [Tu email]  
- 🔗 [LinkedIn](https://www.linkedin.com/in/tu-perfil)

