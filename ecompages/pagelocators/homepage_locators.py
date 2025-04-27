from selenium.webdriver.common.by import By


class HomePageLocator:
    home_page = (By.XPATH, '//a[text()="Home"]')
    album = (By.XPATH, '//a[@data-product_id="24"]')
    beanie_with_logo = (By.XPATH, '//a[@data-product_id="33"]')
    belt = (By.XPATH, '//a[@data-product_id="17"]')
    cap = (By.XPATH, '//a[@data-product_id="18"]')
    polo = (By.XPATH, '//a[@data-product_id="23"]')
    item_total_amount = (By.CLASS_NAME, "woocommerce-Price-amount")
    item_total_count = (By.CSS_SELECTOR, ".count")
    hoodie_with_Zipper = (By.XPATH, '//a[@data-product_id="21"]')
    sunglass = (By.XPATH, '//a[@data-product_id="19"]')
    cart_icon = (By.XPATH, '//a[@title="View your shopping cart"]')
