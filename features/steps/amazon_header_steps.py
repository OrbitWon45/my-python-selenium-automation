from behave import given, when, then
from selenium.webdriver.common.by import By


@given('Open Amazon page')
def open_amazon_page(context):
    context.driver.get('https://www.amazon.com/home')


@when('Search for a table')
def search_on_amazon(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('table')
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@then('Verify search results')
def verify_search_results(context):
    expected_result = '"table"'
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text

    assert expected_result == actual_result, f'Expected result {expected_result} did not match actual result {actual_result}'

