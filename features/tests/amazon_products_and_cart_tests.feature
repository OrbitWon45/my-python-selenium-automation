# Created by white at 10/22/2024
Feature: Amazon products and cart tests

  Scenario: Verify the cart is empty
    Given Open Amazon page
    When Click on cart icon
    Then Verify “Your cart is empty” message is shown