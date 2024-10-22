from behave import given, when, then
from selenium.webdriver.common.by import By


@given('Open Amazon page')
def open_amazon_page(context):
    context.app.header_page.open_url()

@when('Search for a {product}')
def search_on_amazon(context, product):
   context.app.header_page.search_for_product(product)




