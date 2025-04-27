import pytest

from conftest import *
from ecompages.myaccount_page import MyAccount


@pytest.mark.usefixtures("browser_setup")
class TestPrivacypolicy:
    driver = None

    def setup_class(self):
        self.driver.get(BaseUrl)
        self.privacy_contents = MyAccount(self.driver)

    @pytest.mark.tcid4
    def test_privacypolicy_contents(self):
        self.privacy_contents.privacy_policy(expected_content='Oops! That page can’t be found.')

    def teardown_class(self):
        self.driver.quit()

