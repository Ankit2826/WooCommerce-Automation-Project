import time

from ecomhelper.selenium_helper import Seleniumhelper
from ecompages.pagelocators.homepage_locators import HomePageLocator


class HomePage(HomePageLocator, Seleniumhelper):
    driver = None

    def __init__(self, driver):
        super().__init__(driver)

    def add_to_cart(self):
        self.webelement_click(self.home_page)
        self.webelement_click(self.album)
        self.webelement_click(self.cap)
        self.webelement_click(self.polo)
        time.sleep(2)  # Fallen wait

    def verify_cart(self):
        total_count = self.attribute_values(self.item_total_count)
        print(f'\nYour have added {total_count} into your cart.')
        total_price = self.attribute_values(self.item_total_amount)
        print(f'Your total cart value is {total_price}.')
