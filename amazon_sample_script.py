from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
# driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(executable_path=r'C:\Users\white\my-python-selenium-automation\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.amazon.com/')

driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('car')

driver.find_element(By.ID, 'nav-search-submit-button').click()

expected_result = '"car"'
actual_result = driver.find_element(By.XPATH,"//span[@class='a-color-state a-text-bold']").text

sleep(2)

assert expected_result == actual_result, f'Expected result {expected_result} did not match actual result {actual_result}'
print('Test Passed')

driver.quit()