import pytest

from conftest import *
from ecompages.myaccount_page import MyAccount


@pytest.mark.usefixtures("browser_setup")
class TestRegistration:
    driver = None

    def setup_class(self):
        self.driver.get(BaseUrl)
        self.registration_page = MyAccount(self.driver)  # Assign the actual value here

    @pytest.mark.tcid1
    def test_valid_registration(self):
        self.registration_page.registration(email_address, reg_password)

    def teardown_class(self):
        self.driver.quit()
