import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

s = Service("/usr/local/bin/chromedriver") # chromedriver path
driver = webdriver.Chrome(service = s)
base_url = 'https://www.baidu.com'
driver.get(base_url)

driver.implicitly_wait(8)

driver.find_element(By.XPATH, "//*[@id='s-top-loginbtn']").click()
