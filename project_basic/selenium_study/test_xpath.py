from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service("/usr/local/bin/chromedriver") # chromedriver path
driver = webdriver.Chrome(service = s)
base_url = 'https://www.baidu.com'
driver.get(base_url)

driver.implicitly_wait(8)  # time.sleep(30)

# XPATH
# driver.find_element(By.XPATH, "//*[@autocomplete='off']").send_keys("33w")
# driver.find_element(By.LINK_TEXT, "新闻").click()
# driver.find_element(By.ID, "su").click()
# value = driver.find_element(By.XPATH, "//span[text()='按图片搜索']").get_attribute('class')
# print(value)

# CSS

time.sleep(5)
driver.quit()