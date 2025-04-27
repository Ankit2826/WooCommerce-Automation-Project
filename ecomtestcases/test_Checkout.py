import pytest

from conftest import *
from ecompages.cart_page import CartPage

from ecompages.checkout_page import CheckoutPage
from ecompages.home_page import HomePage


@pytest.mark.usefixtures("browser_setup")
class TestAddToCart:
    driver = None

    def setup_class(self):
        self.driver.get(BaseUrl)
        self.home_page = HomePage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)

    @pytest.mark.tcid7
    def test_Checkout(self):
        self.home_page.add_to_cart()
        self.checkout_page.click_checkout_page()
        self.checkout_page.input_billing_info()

    def teardown_class(self):
        self.driver.quit()
