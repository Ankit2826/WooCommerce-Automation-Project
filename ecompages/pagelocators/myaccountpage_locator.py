from selenium.webdriver.common.by import By


class MyAccountPageLocators:
    # Locator
    my_account_xpath = (By.XPATH, '//a[text() = "My account"]')
    username_xpath = (By.XPATH, '//input[@id="username"]')
    password_xpath = (By.XPATH, '//input[@id="password"]')
    show_password_btn_xpath = (By.XPATH, '//span[@class="show-password-input"]')
    remember_checkbox_xpath = (By.XPATH, '//input[@id="rememberme"]')
    login_button_xpath = (By.XPATH, '//button[@name="login"]')
    verify_xpath = (By.XPATH, '//*[@class="entry-title"]')

    # Registration Xpath
    email_field_xpath = (By.XPATH, '//input[@id = "reg_email"]')
    passwd_field_xpath = (By.XPATH, '//input[@id = "reg_password"]')
    show_passwd_btn_xpath = (By.XPATH, "//h2[text()='Register']/following::span[@class='show-password-input'][1]")
    register_btn_xpath = (By.XPATH, '//*[@name = "register"]')
    logout_btn_xpath = (By.XPATH, '//a[text() = "Logout"]')

    # Privacy Policy Content
    privacy_policy_xpath = (By.XPATH, '//a[@target="_blank"]')
    content_xpath = (By.XPATH, '//*[@class="page-title"]')
    error_msg_xpath = (By.XPATH, '//ul[@class="woocommerce-error"]')