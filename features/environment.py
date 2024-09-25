from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def browser_init(context):
    """
    :param context: Behave context
    """
    # driver_path = ChromeDriverManager().install()
    service = Service(executable_path=r'C:\Users\white\my-python-selenium-automation\python-selenium-automation-main\chromedriver-win64\chromedriver.exe')
    context.driver = webdriver.Chrome(service=service)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
