import unittest
from pageobject.bootstrap_page import BoootstrapPage
from pageobject.select_dropdown_page import SelectDropdownPage

class Testmutli(unittest.TestCase):

    def test_01_select_dropdown(self):
        """Select Dropdown Page Testing"""
        sd = SelectDropdownPage()
        sd.select_action("Tuesday", "Ohio")

        # base_url = 'https://demo.seleniumeasy.com/basic-select-dropdown-demo.html'
        # driver.get(base_url)
        # driver.implicitly_wait(3)
        #
        # sel1 = Select(driver.find_element(By.CLASS_NAME, "form-control"))
        # sel1.select_by_value("Monday")
        #
        # sel2 = Select(driver.find_element(By.XPATH,"//*[@id='multi-select']"))
        # sel2.select_by_value("New Jersey")
        #
        # driver.find_element(By.XPATH, "//button[@value='Print All']").click()
        #
        #
        # time.sleep(3)
        # # driver.quit()

    def test_02_bootstrap(self):
        """Bootstrap-Modal Testing"""
        bs = BoootstrapPage()
        bs.bootstrap_action()

        # base_url = 'https://demo.seleniumeasy.com/bootstrap-modal-demo.html'
        # driver.get(base_url)
        # driver.implicitly_wait(3)
        #
        # driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[1]/div/div/div[2]/a").click()
        # time.sleep(1)
        #
        # # use list to find save change button and click
        # save_change = driver.find_elements(By.LINK_TEXT, "Save changes")
        # if len(save_change) > 0:
        #     save_change[0].click()
        # else:
        #     print("no save change link")

        # page_list = driver.find_elements(By.LINK_TEXT, "Select Dropdown List")
        # if len(page_list) > 0:
        #     page_list[0].click()
        # else:
        #     print("no redirect page list")
        #
        # time.sleep(2)
        # driver.quit()

