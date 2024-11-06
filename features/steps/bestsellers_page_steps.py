from behave import given, when, then


@given('Open Amazon page Bestsellers')
def open_amazon_page_bestsellers(context):
    context.app.bestsellers_page.open_url('gp/bestsellers')


@then('Verify the {expected_amount} links are displayed at the top of the B.S. page')
def verify_bestsellers_top_page_links(context,expected_amount):
    context.app.bestsellers_page.verify_bestsellers_top_page_links(expected_amount)