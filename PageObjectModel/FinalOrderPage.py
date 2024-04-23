import time

from PageObjectModel.Locators.Locators import Locators

from selenium.webdriver.common.by import By


class FinalOrderPage(Locators):

    def __init__(self, driver):
        self.driver = driver

    def final_order_confirm(self):
        self.driver.find_element(By.XPATH, self.country_selection_loc_xpath).send_keys("India")
        self.driver.find_element(By.XPATH, self.agree_checkout_loc_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.proceed_button_loc_xpath).click()


