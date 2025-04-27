from ecomhelper.selenium_helper import Seleniumhelper
from ecompages.pagelocators.myaccountpage_locator import MyAccountPageLocators


class MyAccount(MyAccountPageLocators, Seleniumhelper):

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, login_username, login_password):
        # Enter username and password
        self.webelement_enter(self.username_xpath, login_username)
        self.webelement_enter(self.password_xpath, login_password)
        self.webelement_click(self.show_password_btn_xpath)
        self.webelement_click(self.remember_checkbox_xpath)
        self.webelement_click(self.login_button_xpath)
        # Checking error message first
        error_message = self.webelement_text_content(self.error_msg_xpath)

        # If error message is found, login will fail
        if error_message:
            return error_message

        # Check if logout button is present, indicating successful login
        try:
            self.webelement_is_present(self.logout_btn_xpath)
            self.webelement_click(self.logout_btn_xpath)
            return "Login and Logged Out Successful"  # Validation point for valid login

        except TimeoutError:
            return "Login failed - unable to find logout button, unexpected issue"

    def registration(self, reg_email, reg_passwrd):
        self.webelement_enter(self.email_field_xpath, reg_email)
        self.webelement_enter(self.passwd_field_xpath, reg_passwrd)
        self.webelement_click(self.show_passwd_btn_xpath)
        self.webelement_click(self.register_btn_xpath)
        error_message = self.webelement_text_content(self.error_msg_xpath)
        if error_message:
            return error_message
        try:
            self.webelement_is_present(self.logout_btn_xpath)
            self.webelement_click(self.logout_btn_xpath)
            return "Registration and Logged Out Successful"
        except TimeoutError:
            return "Registration failed - unable to find logout button, unexpected issue"

    def privacy_policy(self, expected_content):
        self.webelement_click(self.privacy_policy_xpath)
        self.window_handle()
        self.webelement_text_content(self.content_xpath, expected_content)
