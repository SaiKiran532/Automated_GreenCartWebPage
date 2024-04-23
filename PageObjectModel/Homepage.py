import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from PageObjectModel.Locators.Locators import Locators


class Hompepage(Locators):

    def __init__(self, driver):
        self.driver = driver

    def search_item_input(self, search_text):
        self.driver.find_element(By.XPATH, self.search_loc_xpath).send_keys(search_text)
        time.sleep(2)

    def products_list(self):
        cart = self.driver.find_elements(By.XPATH, self.products_container_loc_xpath)
        count =len(cart)
        assert count > 0
        for items in cart:
            items.find_element(By.XPATH, self.button_loc_xpath).click()

    def proceed_to_checkout(self):
        self.driver.find_element(By.XPATH, self.image_cart_loc_xpath).click()
        self.driver.find_element(By.XPATH, self.proceed_check_out_loc_xpath).click()











