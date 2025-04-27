from selenium.webdriver.common.by import By


class CheckoutPageLocators:
    checkout_page = (By.XPATH, '//a[text()="Checkout"]')
    BILLING_FIRST_NAME = (By.XPATH, '//input[@id="billing_first_name"]')
    BILLING_LAST_NAME = (By.XPATH, '//input[@id="billing_last_name"]')
    BILLING_ADDRESS = (By.XPATH, '//input[@id="billing_address_1"]')
    BILLING_CITY = (By.XPATH, '//input[@id="billing_city"]')
    BILLING_ZIPCODE = (By.XPATH, '//input[@id="billing_postcode"]')
    BILLING_PHONE = (By.XPATH, '//input[@id="billing_phone"]')
    BILLING_EMAIL = (By.XPATH, '//input[@id="billing_email"]')
    Place_order_btn = (By.XPATH, '//button[@id="place_order"]')
    Error_msg = (By.XPATH, '//li[@data-id="billing_postcode"]')
