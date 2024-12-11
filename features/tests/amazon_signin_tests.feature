# Created by white at 11/16/2024
Feature: Signin tests

  Scenario: User can navigate to Signin page
    Given Open Amazon page
    When Click Signin button
    Then Verify Signin page is opened


  Scenario: logged out user navigates to Signin page by clicking orders
    Given Open Amazon page
    When Click Returns and Orders
    Then Verify Signin page is opened


    Scenario: User can navigate to signin page from popup button
      Given Open Amazon page
      When Click signin popup button
      Then Verify Signin page is opened


    Scenario: User sees popup SignIn button and it disappears
      Given Open Amazon page
      Then Verify popup SignIn button is clickable
      When Wait 3 seconds
      Then Verify popup SignIn button is clickable
      And Verify popup SignIn button disappears