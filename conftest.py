import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

from Email_And_Password_Generator import email_id, rand_password

BaseUrl = 'http://demostore.supersqa.com/my-account/'
Url = 'http://demostore.supersqa.com/'


@pytest.fixture(scope="class", autouse=True)
def browser_setup(request):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    # Create the WebDriver instance
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    # Attach driver to the class using request.cls
    request.cls.driver = driver


# ------------------------------------ Test Data ------------------------------------------------------


# Registration test data
email_address = email_id(10)
reg_password = rand_password(12)


