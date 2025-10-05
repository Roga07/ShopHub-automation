Feature: Registro de usuario

  Como un nuevo usuario
  Quiero crear una cuenta
  Para poder acceder a la plataforma

  Background:
    Given que el usuario està en la pagina principal


  Scenario: Registro exitoso
    When el usuario navega a la pagina de registro
    And el usuario completa el formulario de registro con datos vàlidos
    | first_name | last_name | email                | zip_code  | password    |
    | Jhon       | Doe       | jhon.doe@example.com | 12345     | Password123 |

    And el usuario envia el formulario
    Then el usuario deberia ser redirigido a la pagina de registro exitoso
    And se deberia mostrar un mensaje de confirmacion.


  Scenario: Registro con datos invalidos
    When el usuario navega a la pagina de registro
    And el usuario completa el formulario de registro con datos invàlidos
    | first_name | last_name | email                | zip_code  | password    |
    |  Jhon      |  Doe      | jhon.doe.com         | 12345      | 123         |
