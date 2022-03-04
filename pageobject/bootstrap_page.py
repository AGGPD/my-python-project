from base.base_page import Basepage
from selenium.webdriver.common.by import By

class BoootstrapPage(Basepage):

    first_button_loc = (By.XPATH, "/html/body/div[2]/div/div[2]/div[1]/div/div/div[2]/a")
    save_changes_loc = (By.LINK_TEXT, "Save changes")

    def bootstrap_action(self):
        self.url_address("https://demo.seleniumeasy.com/bootstrap-modal-demo.html")
        self.click(BoootstrapPage.first_button_loc)
        self.link_text_choose(BoootstrapPage.save_changes_loc)
 
        self.driver_quit()
