import unittest
from pageobject.input_form_page import InputPage

# global driver
# # open the browser
# s = Service("/usr/local/bin/chromedriver")  # chromedriver path
# driver = webdriver.Chrome(service=s)

class TestInputForm(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_01_input_form(self):
        """Input Form Page Testing"""
        lp = InputPage()
        lp.input_action()

        # self.assertEqual()
        # self.assertTrue()
        # self.assertIn()



    def tearDown(self) -> None:
        pass

        # locate element
        # driver.find_element(By.NAME, 'first_name').send_keys('Andy')
        # driver.find_element(By.NAME, 'last_name').send_keys('Peng')
        # driver.find_element(By.NAME, 'email').send_keys('andypd01@yahoo.com')
        # driver.find_element(By.NAME, 'phone').send_keys('0413989778')
        # driver.find_element(By.NAME, 'address').send_keys('45 fawcett st')
        # driver.find_element(By.NAME, 'city').send_keys('Sydney')
        #
        # select1 = Select(driver.find_element(By.NAME, 'state'))
        # select1.select_by_visible_text('Georgia')
        #
        # driver.find_element(By.NAME, 'zip').send_keys('6100')
        # driver.find_element(By.NAME, 'website').send_keys('www.google.com')
        #
        # driver.find_element(By.XPATH, "//input[@value='yes']").click()
        #
        # driver.find_element(By.NAME, 'comment').send_keys('There is no comment!')
        #
        # driver.find_element(By.XPATH, "//button[@class='btn btn-default']").click()

        # redirect to another page







