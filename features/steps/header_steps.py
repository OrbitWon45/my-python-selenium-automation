from behave import given, when, then
from selenium.webdriver.common.by import By


@given('Open Amazon page')
def open_amazon_page(context):
    context.app.header_page.open_url()


@when('Click signin popup button')
def click_signin_popup_btn(context):
    context.app.header_page.click_signin_popup_btn()




@when('Search for {product}')
def search_on_amazon(context, product):
   context.app.header_page.search_for_product(product)


@when('Click Signin button')
def click_signin_button(context):
    context.app.header_page.click_signin_button()


@when('Click on cart icon')
def click_on_cart(context):
    context.app.header_page.click_on_cart()


@when('Click on Customer Service button')
def click_on_customer_service_button(context):
    context.app.header_page.click_on_customer_service_button()


@then('Cart count shows {expected_amount} items added')
def verify_cart_count(context, expected_amount):
    context.app.header_page.verify_cart_count(expected_amount)