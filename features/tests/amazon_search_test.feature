# Created by white at 10/19/2024
Feature: Tests for amazon search

  Scenario: Verify user can search for a product
    Given Open Amazon page
    When Search for a table
    Then Verify search results