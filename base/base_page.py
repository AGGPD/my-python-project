import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select

class Basepage:

    def __init__(self):
        global driver
        # open the browser
        s = Service("/usr/local/bin/chromedriver")  # chromedriver path
        self.driver = webdriver.Chrome(service=s)
        driver = self.driver
        driver.implicitly_wait(8)

    def url_address(self, url_address):
        self.driver.get(url_address)

        # locate key element
    def locator_element(self, loc):
        return self.driver.find_element(*loc)

    def locator_elements(self,loc):
        return self.driver.find_elements(*loc)

    #setting key element
    def send_keys(self, loc, value):
        self.locator_element(loc).send_keys(value)

    def click(self,loc):
        self.locator_element(loc).click()

    def drop_list_select(self, loc, value):
        sel = Select(self.locator_element(loc))
        sel.select_by_visible_text(value)

    def link_text_choose(self, loc):
        time.sleep(1)
        link_text = self.locator_elements(loc)
        if len(link_text) > 0:
            link_text[0].click()
        else:
            print("no link text found")

    def get_value(self, loc):
       return self.locator_element(loc).text

    def driver_quit(self):
        time.sleep(2)
        self.driver.quit()