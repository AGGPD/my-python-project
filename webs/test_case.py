import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

global driver
# open the browser
s = Service("/usr/local/bin/chromedriver")  # chromedriver path
driver = webdriver.Chrome(service=s)

class TestCase(unittest.TestCase):


    def test_01_login(self):
        global driver
        base_url = 'https://demo.seleniumeasy.com/input-form-demo.html'
        driver.get(base_url)
        # locate element
        driver.find_element(By.NAME, 'first_name').send_keys('Andy')
        driver.find_element(By.NAME, 'last_name').send_keys('Peng')
        driver.find_element(By.NAME, 'email').send_keys('andypd01@yahoo.com')
        driver.find_element(By.NAME, 'phone').send_keys('0413989778')
        driver.find_element(By.NAME, 'address').send_keys('45 fawcett st')
        driver.find_element(By.NAME, 'city').send_keys('Sydney')

        select = Select(driver.find_element(By.NAME, 'state'))
        select.select_by_visible_text('Georgia')

        driver.find_element(By.NAME, 'zip').send_keys('6100')
        driver.find_element(By.NAME, 'website').send_keys('www.google.com')

        # driver.find_elements(By.XPATH, "//*[@value='yes']").click()

        driver.find_element(By.XPATH, "//button[@class='btn btn-default']").click()

        time.sleep(3)
        driver.quit()


    def test02_select_product(self):

        base_url = 'https://demo.seleniumeasy.com/basic-select-dropdown-demo.html'
        driver.get(base_url)
        driver.implicitly_wait(3)



        sel1 = Select(driver.find_element(By.CLASS_NAME, "form-control"))
        sel1.select_by_value("Monday")

        sel2 = Select(driver.find_element(By.XPATH,"//*[@id='multi-select']"))
        sel2.select_by_value("New Jersey")

        driver.find_element(By.XPATH, "//button[@value='Print All']").click()


        time.sleep(3)
        driver.quit()









