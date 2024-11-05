# Created by white at 10/22/2024
Feature: Amazon products and cart tests

  Scenario: Verify the cart is empty
    Given Open Amazon page
    When Click on cart icon
    Then Verify “Your cart is empty” message is shown

  Scenario: Verify user can add a product to cart
    Given Open Amazon page
    When Search for coco coir
    And Choose a product
    And Add product to cart
    Then Verify "Added to cart" message is shown
    And Cart count shows 1 items added


