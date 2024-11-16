# Created by white at 11/16/2024
Feature: Bestsellers tests


  Scenario: Verify the five links exist at the top of Bestsellers page
    Given Open Amazon page Bestsellers
    Then Verify the 5 links are displayed at the top of the B.S. page