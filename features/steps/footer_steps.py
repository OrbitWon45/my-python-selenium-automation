from behave import given,when,then


@then('Verify footer has {expected_amount} links')
def verify_footer_links(context, expected_amount):
    context.app.footer_page.verify_footer_links(expected_amount)