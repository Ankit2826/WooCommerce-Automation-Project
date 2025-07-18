from datetime import datetime
from pathlib import Path
import pytest
import os
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

from Email_And_Password_Generator import email_id, rand_password

BaseUrl = 'http://demostore.supersqa.com/my-account/'
Url = 'http://demostore.supersqa.com/'


# # Create reports folder if not exists
# if not os.path.exists("ecomreports"):
#     os.makedirs("ecomreports")


# Fixture to launch browser
@pytest.fixture(scope="class", autouse=True)
def browser_setup(request):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    request.cls.driver = driver


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    today = datetime.now()
    report_dir = Path("ecomreports", today.strftime("%Y%m%d"))
    report_dir.mkdir(parents=True, exist_ok=True)
    pytest_html = report_dir / f"Report_{today.strftime('%Y%m%d%H%M')}.html"
    config.option.htmlpath = pytest_html
    config.option.self_contained_html = True


def pytest_html_report_title(report):
    report.title = "E COM Test Reports"


# Generate random credentials
email_address = email_id(10)
reg_password = rand_password(12)
