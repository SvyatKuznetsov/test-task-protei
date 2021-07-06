from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from pages.locators import InputsPageLocators


class InputsPage(BasePage):
    def should_be_inputs_page(self):
        self.should_be_main_form()
        self.should_be_email_input()
        self.should_be_name_input()
        self.should_be_gender_selectbox()
        self.should_be_data_11_checkbox()
        self.should_be_data_12_checkbox()
        self.should_be_data_21_radio_button()
        self.should_be_data_22_radio_button()
        self.should_be_data_23_radio_button()
        self.should_be_send_button()
        self.should_be_data_table()

    def should_be_main_form(self):
        assert self.is_element_present(*InputsPageLocators.MAIN_FORM), "There is no inputs page"

    def should_be_email_input(self):
        assert self.is_element_present(*InputsPageLocators.EMAIL_INPUT), "There is no email input"

    def should_be_name_input(self):
        assert self.is_element_present(*InputsPageLocators.NAME_INPUT), "There is no name input"

    def should_be_gender_selectbox(self):
        assert self.is_element_present(*InputsPageLocators.GENDER_SELECTBOX), "There is no gender selectbox"

    def should_be_data_11_checkbox(self):
        assert self.is_element_present(*InputsPageLocators.DATA_11_CHECKBOX), "There is no data 11 selectbox"

    def should_be_data_12_checkbox(self):
        assert self.is_element_present(*InputsPageLocators.DATA_12_CHECKBOX), "There is no data 12 selectbox"

    def should_be_data_21_radio_button(self):
        assert self.is_element_present(*InputsPageLocators.DATA_21_RADIO_BUTTON), "There is no data 21 radio button"

    def should_be_data_22_radio_button(self):
        assert self.is_element_present(*InputsPageLocators.DATA_22_RADIO_BUTTON), "There is no data 22 radio button"

    def should_be_data_23_radio_button(self):
        assert self.is_element_present(*InputsPageLocators.DATA_23_RADIO_BUTTON), "There is no data 23 radio button"

    def should_be_send_button(self):
        assert self.is_element_present(*InputsPageLocators.SEND_BUTTON), "There is no send button"

    def should_be_data_table(self):
        assert self.is_element_present(*InputsPageLocators.DATA_TABLE), "There is no data table"

    def fill_email_input(self, email):
        self.browser.find_element(*InputsPageLocators.EMAIL_INPUT).send_keys(email)

    def fill_name_input(self, name):
        self.browser.find_element(*InputsPageLocators.NAME_INPUT).send_keys(name)

    def get_genders_in_selectbox(self):
        select_item = self.browser.find_element(*InputsPageLocators.GENDER_SELECTBOX)
        return Select(select_item).options

    def select_gender(self, text):
        select_item = self.browser.find_element(*InputsPageLocators.GENDER_SELECTBOX)
        Select(select_item).select_by_visible_text(text)

    def select_data_11_checkbox(self):
        self.browser.find_element(*InputsPageLocators.DATA_11_CHECKBOX).click()

    def select_data_12_checkbox(self):
        self.browser.find_element(*InputsPageLocators.DATA_12_CHECKBOX).click()

    def select_data_21_radio_button(self):
        self.browser.find_element(*InputsPageLocators.DATA_21_RADIO_BUTTON).click()

    def select_data_22_radio_button(self):
        self.browser.find_element(*InputsPageLocators.DATA_22_RADIO_BUTTON).click()

    def select_data_23_radio_button(self):
        self.browser.find_element(*InputsPageLocators.DATA_23_RADIO_BUTTON).click()

    def click_send_button(self):
        self.browser.find_element(*InputsPageLocators.SEND_BUTTON).click()

    def click_successful_add_message_ok_button(self):
        self.browser.find_element(*InputsPageLocators.CLOSE_SUCCESSFUL_ADD_MESSAGE_BUTTON).click()

    def close_message(self):
        self.browser.find_element(*InputsPageLocators.CLOSE_MESSAGE_BUTTON).click()

    def check_successful_add_message(self):
        assert self.is_element_present(*InputsPageLocators.SUCCESSFUL_ADD_MESSAGE), "There is no successful add message"

    def check_wrong_email_format_message(self):
        assert self.is_element_present(*InputsPageLocators.WRONG_EMAIL_FORMAT_MESSAGE), \
            "There is no wrong email format message"

    def check_wrong_empty_name_input_message(self):
        assert self.is_element_present(*InputsPageLocators.EMPTY_NAME_INPUT_MESSAGE), \
            "There is no empty name input message"

    def check_disappearing_successful_add_message(self):
        assert self.is_disappeared(*InputsPageLocators.SUCCESSFUL_ADD_MESSAGE), \
            "Successful add message didn`t disappearing, but should"

    def check_disappearing_wrong_email_format_message(self):
        assert self.is_disappeared(*InputsPageLocators.WRONG_EMAIL_FORMAT_MESSAGE), \
            "Wrong email format message didn`t disappearing, but should"

    def check_disappearing_empty_name_input_message(self):
        assert self.is_disappeared(*InputsPageLocators.EMPTY_NAME_INPUT_MESSAGE), \
            "Wrong empty name input message didn`t disappearing, but should"

    def get_data_from_table(self, index_table):
        locator = InputsPageLocators.NEW_ADDED_TABLE
        locator = (locator[0], locator[1] + f"({index_table})")
        return self.browser.find_element(*locator).text.split()

    def check_email_in_table(self, email_in_input, index_table):
        email_in_table = self.get_data_from_table(index_table)[0]
        assert email_in_table == email_in_input, "Emails don`t match"

    def check_name_in_table(self, name_in_input, index_table):
        name_in_table = self.get_data_from_table(index_table)[1]
        assert name_in_table == name_in_input, "Names don`t match"

    def check_gender_in_table(self, gender_in_input, index_table):
        gender_in_table = self.get_data_from_table(index_table)[2]
        assert gender_in_table == gender_in_input, "Genders don`t match"

    def check_choice_1_with_1_selected_options(self, choice_text_in_input, index_table):
        choice_text_in_table = self.get_data_from_table(index_table)[3]
        assert choice_text_in_table == choice_text_in_input, "Choices don`t match"

    def check_choice_1_with_2_selected_options(self, index_table):
        choices_text_in_table = self.get_data_from_table(index_table)[3:5]
        choices_text_in_table = " ".join(choices_text_in_table)
        choices_text_in_input = "1.1, 1.2"
        assert choices_text_in_table == choices_text_in_input, "Choices don`t match"

    def check_choice_2(self, choice_text_in_input, index_table):
        choice_text_in_table = self.get_data_from_table(index_table)[-1]
        if choice_text_in_input == '':
            # если ничего не выбрано, то последнего элемента в таблице не будет из-за использования сплита
            # поэтому сравниваем, что тексты не равны
            assert choice_text_in_table != choice_text_in_input, "Choices don`t match"
        else:
            assert choice_text_in_table == choice_text_in_input, "Choices don`t match"

