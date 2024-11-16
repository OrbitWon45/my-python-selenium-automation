from behave import given, when, then
from time import sleep


@then('Verify the {expected_amount} links are displayed at the top of the C.S. page')
def verify_customer_service_top_page_links(context,expected_amount):
    context.app.customer_service_page.verify_customer_service_top_page_links(expected_amount)


@then('Verify all text elements are displayed')
def verify_all_text_elements(context):
    context.app.customer_service_page.verify_all_text_elements()


@then('Verify {expected_amount} Welcome links are displayed')
def verify_welcome_links(context, expected_amount):
    context.app.customer_service_page.verify_welcome_links(expected_amount)


@then('Verify search field is displayed')
def verify_search_field_is_displayed(context):
    context.app.customer_service_page.verify_search_field_is_displayed()


@then('Verify {expected_amount} All Help Topic links are displayed')
def verify_all_help_links_are_displayed(context, expected_amount):
    context.app.customer_service_page.verify_all_help_links_are_displayed(expected_amount)