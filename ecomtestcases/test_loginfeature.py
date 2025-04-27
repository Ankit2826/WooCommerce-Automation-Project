import pytest

from conftest import *
from ecompages.myaccount_page import *


@pytest.mark.usefixtures("browser_setup")
class Test_login:
    driver = None

    def setup_class(self):
        self.driver.get(BaseUrl)
        self.login_page = MyAccount(self.driver)

    @pytest.mark.tcid2
    def test_valid_login(self):
        self.login_page.login('logintestdata@gmail.com', 'Password#123456')

    @pytest.mark.tcid3
    def test_none_registeredUser_login(self):
        expected_message = 'Unknown email address. Check again or try your username.'
        result = self.login_page.login('invalidtestdata@gmail.com', 'Password#12')

        assert result == expected_message, f"Expected: '{expected_message}', but got: '{result}'"

    def teardown_class(self):
        self.driver.quit()
