from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service('../drivers/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get('http://www.googel.com')

