from ecomhelper.selenium_helper import Seleniumhelper
from ecompages.pagelocators.checkoutpage_locator import CheckoutPageLocators
from conftest import *


class CheckoutPage(CheckoutPageLocators, Seleniumhelper):
    driver = None

    def __init__(self, driver):
        super().__init__(driver)

    def click_checkout_page(self):
        self.webelement_click(self.checkout_page)

    def input_billing_info(self):
        self.webelement_enter(self.BILLING_FIRST_NAME, 'TestFirstName')
        self.webelement_enter(self.BILLING_LAST_NAME, 'Automation')
        self.webelement_enter(self.BILLING_ADDRESS, '123 Main Street')
        self.webelement_enter(self.BILLING_CITY, 'San Francisco')
        self.webelement_enter(self.BILLING_ZIPCODE, '125632')
        self.webelement_enter(self.BILLING_PHONE, '3215896420')
        self.webelement_enter(self.BILLING_EMAIL, email_address)

    def click_placeorder(self):
        self.webelement_click(self.Place_order_btn)

