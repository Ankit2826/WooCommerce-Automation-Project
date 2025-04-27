from ecomhelper.selenium_helper import Seleniumhelper
from ecompages.pagelocators.cartpage_locator import CartPageLocator


class CartPage(CartPageLocator, Seleniumhelper):
    driver = None

    def __init__(self, driver):
        super().__init__(driver)

    def verify_coupon(self):
        self.webelement_click(self.cart_page)
        self.webelement_enter(self.coupon_code, 'ssqa100')
        self.webelement_click(self.apply_btn)
        self.webelement_text_content(self.cartpage_message, 'Coupon code applied successfully.')
