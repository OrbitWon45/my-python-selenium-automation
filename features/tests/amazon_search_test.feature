# Created by white at 10/19/2024
Feature: Tests for Amazon search

  Scenario: Verify user can search for Coco Coir
    Given Open Amazon page
    When Search for coco coir
    Then Verify search results "coco coir"

  Scenario Outline: Verify user can search for a product
    Given Open Amazon page
    When Search for <search_product>
    Then Verify search results <search_result>
    Examples:
    |search_product  |search_result |
    |table           |"table"       |
    |car             |"car"         |
    |coco coir       |"coco coir"   |