import time

from conftest import email_address
from ecompages.pagelocators.checkoutpage_locator import CheckoutPageLocators
from ecompages.pagelocators.homepage_locators import HomePageLocator
from ecompages.pagelocators.cartpage_locator import CartPageLocator
from ecomhelper.selenium_helper import Seleniumhelper
from ecompages.pagelocators.OrderReceivedPage_locators import OrderReceivedPage


class EndToEndCheckout(HomePageLocator, CartPageLocator, CheckoutPageLocators, OrderReceivedPage, Seleniumhelper):
    driver = None

    def __init__(self, driver):
        super().__init__(driver)

    def guest_add_to_cart(self):
        self.webelement_click(self.album)
        self.webelement_click(self.hoodie_with_Zipper)
        self.webelement_click(self.cap)
        self.webelement_click(self.polo)
        self.webelement_click(self.sunglass)

    def guest_verify_cart(self, count):
        expected_text = str(count) + ' items'
        self.wait_until_element_contain_text(self.item_total_count, expected_text)

    def guest_click_cart_icon(self):
        self.webelement_click(self.cart_icon)

    def guest_apply_coupon(self):
        self.webelement_enter(self.coupon_code, 'ssqa100')
        self.webelement_click(self.apply_btn)
        self.webelement_click(self.cart_page_checkout_btn)

    def guest_input_billing_info(self):
        self.webelement_enter(self.BILLING_FIRST_NAME, 'TestFirstName')
        self.webelement_enter(self.BILLING_LAST_NAME, 'Automation')
        self.webelement_enter(self.BILLING_ADDRESS, '123 Main Street')
        self.webelement_enter(self.BILLING_CITY, 'San Francisco')
        self.webelement_enter(self.BILLING_ZIPCODE, '10004')
        self.webelement_enter(self.BILLING_PHONE, '3215896420')
        self.webelement_enter(self.BILLING_EMAIL, email_address)

    def guest_click_placeorder(self):
        self.webelement_click(self.Place_order_btn)
        # self.webelement_is_present(self.Error_msg)
        # assert "Invalid ZIP Code"

    def guest_verify_order_received(self):
        self.attribute_values(self.msg_1)

