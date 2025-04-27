import pytest

from conftest import *

from ecompages.cart_page import *
from ecompages.home_page import *


@pytest.mark.usefixtures("browser_setup")
class TestAddToCart:
    driver = None

    def setup_class(self):
        self.driver.get(BaseUrl)
        self.home_page = HomePage(self.driver)
        self.cart_page = CartPage(self.driver)

    @pytest.mark.tcid6
    def test_coupon(self):
        self.home_page.add_to_cart()
        self.cart_page.verify_coupon()

    def teardown_class(self):
        self.driver.quit()
