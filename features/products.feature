Feature: Gestión de productos

  Como usuario
  Quiero ver y agregar productos al carrito
  Para poder realizar compras en la plataforma

  Background:
    Given que el usuario está en la página principal

  Scenario: Visualización de productos disponibles
    When el usuario navega a la página de productos
    Then debería visualizar una lista de productos disponibles
    And agregara al carrito desde la lista de productos

  Scenario: Visualización de detalles de un producto
    Given que el usuario está en la página de productos
    When el usuario selecciona un producto
    Then debería visualizar la página de detalles del producto
    And debería mostrarse el nombre, precio, descripción e imagen del producto

