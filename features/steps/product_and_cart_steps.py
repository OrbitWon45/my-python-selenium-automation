from behave import given, when, then

@then('Verify “Your cart is empty” message is shown')
def verify_cart_is_empty(context):
    context.app.product_and_cart_page.verify_cart_is_empty()