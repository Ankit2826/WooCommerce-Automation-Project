from selenium.webdriver.common.by import By


class CartPageLocator:
    cart_page = (By.XPATH, '//a[text()="Cart"]')
    coupon_code = (By.XPATH, '//input[@name="coupon_code"]')
    apply_btn = (By.XPATH, '//button[@name="apply_coupon"]')
    cartpage_message = (By.XPATH, '//div[@class="woocommerce-message"]')
    cart_page_checkout_btn = (By.XPATH, '//div[@class="wc-proceed-to-checkout"]')

