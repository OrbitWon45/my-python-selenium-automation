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

driver.get('https://www.amazon.com/home')
sleep(3)
driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('car')

driver.find_element(By.ID, 'nav-search-submit-button').click()

expected_result = '"car"'
actual_result = driver.find_element(By.XPATH,"//span[@class='a-color-state a-text-bold']").text

sleep(2)

assert expected_result == actual_result, f'Expected result {expected_result} did not match actual result {actual_result}'
print('Test Passed')

driver.get('https://www.amazon.com/dp/B0D9RR2Y9K')
sleep(2)
driver.refresh()
colors = driver.find_elements(By.CSS_SELECTOR, 'div#variation_color_name li')

for color in colors:
    color.click()
    current_color = driver.find_element(By.XPATH,'//div[@id="variation_color_name"]//span[@class="selection"]').text
    print(current_color)

driver.quit()