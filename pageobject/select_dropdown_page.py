from base.base_page import Basepage
from selenium.webdriver.common.by import By

class SelectDropdownPage(Basepage):

    day_select_loc = (By.CLASS_NAME, "form-control")
    city_select_loc = (By.XPATH,"//*[@id='multi-select']")
    submit_loc = (By.XPATH, "//button[@value='Print All']")

    def select_action(self, day_value, city_value):
        self.url_address('https://demo.seleniumeasy.com/basic-select-dropdown-demo.html')
        self.drop_list_select(SelectDropdownPage.day_select_loc, day_value)
        self.drop_list_select(SelectDropdownPage.city_select_loc, city_value)
        self.click(SelectDropdownPage.submit_loc)

        self.driver_quit()




