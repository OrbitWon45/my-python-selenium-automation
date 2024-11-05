from behave import given, when, then


@when('Add product to cart')
def add_to_cart(context):
    context.app.product_and_cart_page.add_to_cart_coco()


@then('Verify "Added to cart" message is shown')
def verify_added_to_cart_msg(context):
    context.app.product_and_cart_page.verify_added_to_cart_msg()


@then('Verify “Your cart is empty” message is shown')
def verify_cart_is_empty(context):
    context.app.product_and_cart_page.verify_cart_is_empty()


@then('Cart count shows {expected_amount} items added')
def verify_cart_count(context, expected_amount):
    context.app.product_and_cart_page.verify_cart_count(expected_amount)




