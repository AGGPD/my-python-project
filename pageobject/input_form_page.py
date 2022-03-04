from base.base_page import Basepage
from selenium.webdriver.common.by import By
import time

class InputPage(Basepage):

    # page element
    firstname_loc = (By.NAME, 'first_name')
    lastname_loc = (By.NAME, 'last_name')
    email_loc = (By.NAME, 'email')
    phone_loc = (By.NAME, 'phone')
    address_loc = (By.NAME, 'address')
    city_loc = (By.NAME, 'city')
    state_list_loc = (By.NAME, 'state')
    zip_loc = (By.NAME, 'zip')
    website_loc = (By.NAME, 'website')
    host_loc = (By.XPATH, "//input[@value='yes']")
    comment_loc = (By.NAME, 'comment')
    submit_loc = (By.XPATH, "//button[@class='btn btn-default']")
    #page action

    def input_action(self):

        self.url_address("https://demo.seleniumeasy.com/input-form-demo.html")
        # use self function send_keys
        self.send_keys(InputPage.firstname_loc, 'Andy')
        self.send_keys(InputPage.lastname_loc, 'Peng')
        self.send_keys(InputPage.email_loc, 'andypd01@yahoo.com')
        self.send_keys(InputPage.phone_loc, '0413989778')
        self.send_keys(InputPage.address_loc, '16 Epping Rd')
        self.send_keys(InputPage.city_loc, 'Sydney')
        self.drop_list_select(InputPage.state_list_loc, 'Georgia') # use function drop_list_select
        self.send_keys(InputPage.zip_loc, '2000')
        self.send_keys(InputPage.website_loc, 'www.google.com')
        self.click(InputPage.host_loc) # use self function click
        self.send_keys(InputPage.comment_loc, 'No Comment')
        self.click(InputPage.submit_loc)

        self.driver_quit()



