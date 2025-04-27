import pytest

from conftest import *
from ecompages.home_page import *


@pytest.mark.usefixtures("browser_setup")
class TestAddToCart:
    driver = None

    def setup_class(self):
        self.driver.get(BaseUrl)
        self.home_page = HomePage(self.driver)

    @pytest.mark.tcid5
    def test_AddToCart(self):
        self.home_page.add_to_cart()
        self.home_page.verify_cart()

    def teardown_class(self):
        self.driver.quit()
