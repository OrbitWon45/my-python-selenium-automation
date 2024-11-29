from behave import given, when, then


@given('Open Amazon product {product} page')
def open_amazon_product_page(context, product):
    context.app.product_and_cart_page.open_url(f'dp/{product}')


@when('Add product to cart')
def add_to_cart(context):
    context.app.product_and_cart_page.add_to_cart_coco()


@when('Store product name')
def store_product_name(context):
    context.app.product_and_cart_page.store_product_name()


@then('Verify "Added to cart" message is shown')
def verify_added_to_cart_msg(context):
    context.app.product_and_cart_page.verify_added_to_cart_msg()


@then('Verify “Your cart is empty” message is shown')
def verify_cart_is_empty(context):
    context.app.product_and_cart_page.verify_cart_is_empty()


@then('Verify correct product is added to cart')
def verify_product_is_added_to_cart(context):
    context.app.product_and_cart_page.verify_product_is_added_to_cart()


@then('Verify user can click through options')
def verify_user_can_click_thr_options(context):
    context.app.product_and_cart_page.verify_user_can_click_thr_options()



