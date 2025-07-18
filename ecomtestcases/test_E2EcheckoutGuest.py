from conftest import *
from ecompages.E2E_checkout_guest_user import EndToEndCheckout
from ecompages.checkout_page import *


@pytest.mark.usefixtures("browser_setup")
class TestAddToCart:
    driver = None

    def setup_class(self):
        self.driver.get(Url)
        self.guest_checkout = EndToEndCheckout(self.driver)

    @pytest.mark.tcid8
    def test_E2E_Checkout_Guest(self):
        # add item to cart
        self.guest_checkout.guest_add_to_cart()
        # verify cart
        self.guest_checkout.guest_verify_cart(5)
        # click on cart icon
        self.guest_checkout.guest_click_cart_icon()
        # apply free coupon
        self.guest_checkout.guest_apply_coupon()
        # fill in form
        self.guest_checkout.guest_input_billing_info()
        # click on place order
        self.guest_checkout.guest_click_placeorder()
        # verify order is received
        self.guest_checkout.guest_verify_order_received()

    def teardown_class(self):
        self.driver.quit()
