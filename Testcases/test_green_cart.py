import time

import pytest
from selenium import webdriver
from PageObjectModel.Homepage import Hompepage
from PageObjectModel.CartCheckOutPage import CartCheckOutPage
from PageObjectModel.FinalOrderPage import FinalOrderPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class TestGreenCart:
    pageurl = ReadConfig.get_Application_url()
    logger = LogGen.log_gen()
    searchtext = ReadConfig.get_search_text()
    promocode = ReadConfig.get_promo_code()
    logger = LogGen.log_gen()

    scree_shot_path = "C:\\Users\\saikiran.challa\\PycharmProjects\\pythonProject6\\Screenshots\\test_home_page.png"

    def test_home_page(self, setup):
        self.logger.info("********** GreenCartTest ********** ")
        self.logger.info("********** Opening page Url **********")
        self.driver = setup
        self.driver.get(self.pageurl)

        self.hp = Hompepage(self.driver)
        self.logger.info("********** Searching text **********")
        self.hp.search_item_input(self.searchtext)

        self.logger.info("********** Adding Items to cart **********")
        self.hp.products_list()

        self.hp.proceed_to_checkout()
        self.logger.info("********** Checkout proceeded **********")

        self.logger.info("********** Applying Promocode **********")
        self.cp = CartCheckOutPage(self.driver)
        self.cp.apply_promo_code(self.promocode)

        self.fp = FinalOrderPage(self.driver)
        self.logger.info("********** Confirming Order **********")
        self.fp.final_order_confirm()
        actual_title1 = self.driver.title
        if actual_title1 == "GreenKart - veg and fruits kart":
            self.driver.save_screenshot(self.scree_shot_path)
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(self.scree_shot_path)
            self.driver.close()
            assert False

        self.logger.info("********** Testcase Passed **********")









