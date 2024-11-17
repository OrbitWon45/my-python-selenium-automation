from behave import given, when, then
from time import sleep


@when('Choose a coco coir product')
def choose_a_product_coco(context):
    context.app.product_and_cart_page.choose_a_product_coco()


@then('Verify search results {expected_result}')
def verify_search_results(context, expected_result):
    context.app.search_results_page.verify_search_results(expected_result)