from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
# driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(executable_path=r'C:\Users\white\my-python-selenium-automation\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(5)
driver.wait = WebDriverWait(driver, 10)

search_btn = (By.NAME, 'btnK')

# open the url
driver.get('https://www.google.com/')

# populate search field
search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('car')

# Has to be defined in code where the wait is used
# it waits for the condition to be met every 500 ms
# always fails with timeout exception
# supports custom conditions, usually taken from EC
# click search button
driver.wait.until(EC.element_to_be_clickable(search_btn), message='Search btn not clickable').click()

# verify search results
assert 'car'.lower() in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
