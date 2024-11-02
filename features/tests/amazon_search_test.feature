# Created by white at 10/19/2024
Feature: Tests for Amazon search

  Scenario Outline: Verify user can search for a product
    Given Open Amazon page
    When Search for a <search_product>
    Then Verify search results <search_result>
    Examples:
    |search_product  |search_result |
    |table           |"table"       |
    |car             |"car"         |
    |coco coir       |"coco coir"   |