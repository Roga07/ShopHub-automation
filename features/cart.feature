Feature: Carrito de compras

  Como usuario
  Quiero gestionar los productos en mi carrito
  Para revisar, modificar o eliminar mis selecciones antes de comprar

  Background:
    Given que el usuario ha iniciado sesión
    And que el usuario tiene al menos un producto en el carrito

  Scenario: Proceder al pago
    Given que el usuario está en la página del carrito
    When el usuario hace clic en el botón "Proceder al pago"
    Then debería ser redirigido a la página de checkout


  Scenario: Aumentar cantidad de un producto
    Given que el usuario está en la página del carrito
    When el usuario incrementa la cantidad de un producto
    Then el subtotal y el total general deberían actualizarse correctamente



