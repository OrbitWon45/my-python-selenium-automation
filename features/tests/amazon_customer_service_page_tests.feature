# Created by white at 11/6/2024
Feature: Customer Service page tests

  Scenario: Verify all elements are present on Customer Service page
    Given Open Amazon page
    When Click on Customer Service button
    Then Verify the 3 links are displayed at the top of the C.S. page
    And Verify all text elements are displayed
    And Verify 11 Welcome links are displayed
    And Verify search field is displayed
    And Verify 11 All Help Topic links are displayed