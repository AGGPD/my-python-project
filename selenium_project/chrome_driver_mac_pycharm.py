from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')

s = Service("/usr/local/bin/chromedriver") # chromedriver完整路径
driver = webdriver.Chrome(service = s)

base_url = 'https://www.booking.com'
driver.get(base_url)



#  driver.quit()