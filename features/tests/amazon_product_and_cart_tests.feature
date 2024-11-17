# Created by white at 11/16/2024
Feature: Amazon product and cart tests


  Scenario: Verify the cart is empty
    Given Open Amazon page
    When Click on cart icon
    Then Verify “Your cart is empty” message is shown
    And Cart count shows 0 items added

  Scenario: Verify user can add a product to cart
    Given Open Amazon page
    When Search for coco coir
    And Choose a coco coir product
    And Add product to cart
    Then Verify "Added to cart" message is shown
    And Cart count shows 1 items added


  Scenario: Verify correct product is added to cart
    Given Open Amazon page
    When Search for coco coir
    And Choose a coco coir product
    And Store product name
    And Add product to cart
    And Click on cart icon
    Then Verify correct product is added to cart