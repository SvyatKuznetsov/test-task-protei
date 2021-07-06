from pages.locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()

    def should_be_login_url(self):
        assert "qa-test" in self.browser.current_url, "Opened not login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_INPUT), "There is no email input"
        assert self.is_element_present(*LoginPageLocators.PASS_INPUT), "There is no pass input"
        assert self.is_element_present(*LoginPageLocators.AUTH_BUTTON), "There is no auth button"

    def fill_email_input(self, email):
        self.browser.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)

    def fill_pass_input(self, password):
        self.browser.find_element(*LoginPageLocators.PASS_INPUT).send_keys(password)

    def fill_all_inputs(self, email, password):
        self.fill_email_input(email)
        self.fill_pass_input(password)

    def clear_all_inputs(self):
        self.browser.find_element(*LoginPageLocators.EMAIL_INPUT).clear()
        self.browser.find_element(*LoginPageLocators.PASS_INPUT).clear()

    def click_authorize_button(self):
        self.browser.find_element(*LoginPageLocators.AUTH_BUTTON).click()

    def close_message(self):
        self.browser.find_element(*LoginPageLocators.CLOSE_MESSAGE_BUTTON).click()

    def check_wrong_data_message(self):
        assert self.is_element_present(*LoginPageLocators.WRONG_DATA_MESSAGE), "There is no wrong data message"

    def check_wrong_email_format_message(self):
        assert self.is_element_present(*LoginPageLocators.WRONG_EMAIL_FORMAT_MESSAGE), \
            "There is no wrong email format message"

    def check_disappearing_wrong_data_message(self):
        assert self.is_disappeared(*LoginPageLocators.WRONG_DATA_MESSAGE), \
            "Wrong data message didn`t disappearing, but should"

    def check_disappearing_wrong_email_format_message(self):
        assert self.is_disappeared(*LoginPageLocators.WRONG_EMAIL_FORMAT_MESSAGE), \
            "Wrong email format message didn`t disappearing, but should"

    def authorize_user(self):
        self.fill_all_inputs("test@protei.ru", "test")
        self.click_authorize_button()
