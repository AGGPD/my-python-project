from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


s = Service('../../drivers/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get('https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html')


driver.implicitly_wait(8)  # time.sleep(30)
my_element = driver.find_element(By.ID, 'downloadButton')
my_element.click()

# progress_element = driver.find_element(By.CLASS_NAME, 'progress-label')
# print(f"{progress_element.text == 'Complete!'}")

results = WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'progress-label'),  # Element filtration
        'Complete!'  # the expected text
    )
)

print(results)
if results == True:
    time.sleep(8)
    driver.quit()