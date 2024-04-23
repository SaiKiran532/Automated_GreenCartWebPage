import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjectModel.Locators.Locators import Locators


class CartCheckOutPage(Locators):

    def __init__(self, driver):
        self.driver = driver

    def apply_promo_code(self, promocode):
        self.driver.find_element(By.XPATH, self.promocode_input_loc_xpath).send_keys(promocode)
        self.driver.find_element(By.XPATH, self.promo_button_loc_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, self.promo_info_loc_css_selector)))
        cart = self.driver.find_elements(By.XPATH, self.cart_items_loc_xpath)
        sum = 0
        for item in cart:
            sum = sum + int(item.text)
        total_sum = self.driver.find_element(By.XPATH, self.total_sum_loc_xpath).text
        assert int(total_sum) == sum

        discount_amount = self.driver.find_element(By.XPATH, self.discount_amt_loc_xpath).text
        assert float(discount_amount) < int(total_sum)
        print(self.driver.find_element(By.CSS_SELECTOR, self.promo_info_loc_css_selector).text)
        self.driver.find_element(By.XPATH, self.place_order_loc_xpath).click()
