Feature: Inicio de sesión

  Como usuario registrado
  Quiero iniciar sesión en la plataforma
  Para acceder a mi cuenta y usar sus funcionalidades

  Background:
    Given que el usuario está en la página principal

  Scenario: Inicio de sesión exitoso
    When el usuario navega a la página de inicio de sesión
    And el usuario ingresa credenciales válidas
      | email                | password     |
      | jhon.doe@example.com | Password123  |
    And el usuario hace clic en el botón de iniciar sesión
    Then el usuario debería ser redirigido al panel principal
    And se debería mostrar un mensaje de bienvenida

  Scenario: Inicio de sesión con credenciales no registrado
  When el usuario navega a la página de inicio de sesión
  And el usuario ingresa credenciales no registrados
    | email                      | password     |
    | dhani.doe@example.com      | Password123  |
  And el usuario hace clic en el botón de iniciar sesión
  Then debería mostrarse un mensaje de error indicando "Credenciales inválidas"
