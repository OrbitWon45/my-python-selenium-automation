from behave import given, when, then


@then('Verify Signin page is opened')
def verify_signin_page_is_open(context):
    context.app.signin_page.verify_signin_page_is_open()
