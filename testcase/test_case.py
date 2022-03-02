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


    def test_01_input_form(self):

        base_url = 'https://demo.seleniumeasy.com/input-form-demo.html'
        driver.get(base_url)
        # locate element
        driver.find_element(By.NAME, 'first_name').send_keys('Andy')
        driver.find_element(By.NAME, 'last_name').send_keys('Peng')
        driver.find_element(By.NAME, 'email').send_keys('andypd01@yahoo.com')
        driver.find_element(By.NAME, 'phone').send_keys('0413989778')
        driver.find_element(By.NAME, 'address').send_keys('45 fawcett st')
        driver.find_element(By.NAME, 'city').send_keys('Sydney')

        select1 = Select(driver.find_element(By.NAME, 'state'))
        select1.select_by_visible_text('Georgia')

        driver.find_element(By.NAME, 'zip').send_keys('6100')
        driver.find_element(By.NAME, 'website').send_keys('www.google.com')

        driver.find_element(By.XPATH, "//input[@value='yes']").click()

        driver.find_element(By.NAME, 'comment').send_keys('There is no comment!')

        driver.find_element(By.XPATH, "//button[@class='btn btn-default']").click()

        # redirect to another page
        page_list = driver.find_elements(By.PARTIAL_LINK_TEXT, "Select Dropdown List")
        if len(page_list) > 0:
            page_list[0].click()
        else:
            print("no redirect page link")


        time.sleep(3)
        driver.quit()


    def test_02_select_dropdown(self):

        base_url = 'https://demo.seleniumeasy.com/basic-select-dropdown-demo.html'
        driver.get(base_url)
        driver.implicitly_wait(3)

        sel1 = Select(driver.find_element(By.CLASS_NAME, "form-control"))
        sel1.select_by_value("Monday")

        sel2 = Select(driver.find_element(By.XPATH,"//*[@id='multi-select']"))
        sel2.select_by_value("New Jersey")

        driver.find_element(By.XPATH, "//button[@value='Print All']").click()


        time.sleep(3)
        # driver.quit()


    def test_03_bootstrap(self):

        base_url = 'https://demo.seleniumeasy.com/bootstrap-modal-demo.html'
        driver.get(base_url)
        driver.implicitly_wait(3)

        driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[1]/div/div/div[2]/a").click()
        time.sleep(1)

        # use list to find save change button and click
        save_change = driver.find_elements(By.LINK_TEXT, "Save changes")
        if len(save_change) > 0:
            save_change[0].click()
        else:
            print("no save change link")

        page_list = driver.find_elements(By.LINK_TEXT, "Select Dropdown List")
        if len(page_list) > 0:
            page_list[0].click()
        else:
            print("no redirect page list")

        time.sleep(2)
        driver.quit()

