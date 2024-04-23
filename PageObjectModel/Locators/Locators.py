class Locators:
    # Homepage locators
    search_loc_xpath = "//input[@type='search']"
    products_container_loc_xpath = "//div[@class='products']/div"
    button_loc_xpath = "div/button"
    image_cart_loc_xpath = "//img[@alt='Cart']/..//img[@alt='Cart']"
    proceed_check_out_loc_xpath = "//button[contains(text(),'PROCEED TO CHECKOUT')]"

    # CartCheckOutPage locators
    promocode_input_loc_xpath = "//input[@class='promoCode']"
    promo_button_loc_xpath = "//button[@class='promoBtn']"
    promo_info_loc_css_selector = ".promoInfo"
    cart_items_loc_xpath = "//tr/td[5]/p"
    total_sum_loc_xpath = "//span[@class='totAmt']"
    discount_amt_loc_xpath = "//span[@class='discountAmt']"
    place_order_loc_xpath = "//button[contains(text(),'Place Order')]"
    country_selection_loc_xpath = "//select[@style='width: 200px;']"
    agree_checkout_loc_xpath = "//input[@class='chkAgree']"
    proceed_button_loc_xpath = "//button[contains(text(),'Proceed')]"