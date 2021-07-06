import pytest

from pages.inputs_page import InputsPage
from pages.login_page import LoginPage


@pytest.fixture(scope="function", autouse=True)
def setup(browser):
    link = "D:\Python\\test-task-protei-git\qa-test.html"
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.authorize_user()
    page = InputsPage(browser, browser.current_url)
    page.should_be_inputs_page()
    return page


# успешное добавление со всеми заполненными данными
def test_user_can_add_all_correct_data(browser, setup):
    page = setup
    page.fill_email_input("123@mail.ru")
    page.fill_name_input("name")
    web_elements = page.get_genders_in_selectbox()
    genders = [el.text for el in web_elements]
    gender = genders[0]
    page.select_gender(gender)
    page.select_data_11_checkbox()
    page.select_data_12_checkbox()
    page.select_data_22_radio_button()
    page.click_send_button()
    page.check_successful_add_message()


# возможность закрыть всплывающее окно об успешном добавлении
def test_user_can_close_successful_add_message(browser, setup):
    page = setup
    page.fill_email_input("123@mail.ru")
    page.fill_name_input("name")
    web_elements = page.get_genders_in_selectbox()
    genders = [el.text for el in web_elements]
    gender = genders[0]
    page.select_gender(gender)
    page.select_data_11_checkbox()
    page.select_data_12_checkbox()
    page.select_data_22_radio_button()
    page.click_send_button()
    page.check_successful_add_message()
    page.click_successful_add_message_ok_button()
    page.check_disappearing_successful_add_message()


# добавленная запись видна в таблице
# выбраны все чекбоксы
def test_user_can_see_all_filled_data_in_table(browser, setup):
    page = setup
    email = "123@mail.ru"
    name = "name"
    web_elements = page.get_genders_in_selectbox()
    genders = [el.text for el in web_elements]
    gender = genders[0]
    page.fill_email_input(email)
    page.fill_name_input(name)
    page.select_gender(gender)
    page.select_data_11_checkbox()
    page.select_data_12_checkbox()
    page.select_data_22_radio_button()
    page.click_send_button()
    page.check_successful_add_message()
    page.click_successful_add_message_ok_button()
    page.check_disappearing_successful_add_message()
    page.check_email_in_table(email, 1)
    page.check_name_in_table(name, 1)
    page.check_gender_in_table(gender, 1)
    page.check_choice_1_with_2_selected_options(1)
    page.check_choice_2("2.2", 1)


# добавленная запись видна в таблице
# в 1-м чекбоксе выбрана только одна запись
def test_user_can_see_added_data_in_table_with_selected_1_option_in_choice_1(browser, setup):
    page = setup
    email = "123@mail.ru"
    name = "name"
    web_elements = page.get_genders_in_selectbox()
    genders = [el.text for el in web_elements]
    gender = genders[0]
    page.fill_email_input(email)
    page.fill_name_input(name)
    page.select_gender(gender)
    page.select_data_11_checkbox()
    page.select_data_22_radio_button()
    page.click_send_button()
    page.check_successful_add_message()
    page.click_successful_add_message_ok_button()
    page.check_disappearing_successful_add_message()
    page.check_email_in_table(email, 1)
    page.check_name_in_table(name, 1)
    page.check_gender_in_table(gender, 1)
    page.check_choice_1_with_1_selected_options("1.1", 1)
    page.check_choice_2("2.2", 1)


# добавленная запись видна в таблице
# в 1-м чекбоксе ничего не выбрано, выбран только 2-й чекбокс
def test_user_can_see_added_data_in_table_with_selected_only_choice_2(browser, setup):
    page = setup
    email = "123@mail.ru"
    name = "name"
    web_elements = page.get_genders_in_selectbox()
    genders = [el.text for el in web_elements]
    gender = genders[0]
    page.fill_email_input(email)
    page.fill_name_input(name)
    page.select_gender(gender)
    page.select_data_22_radio_button()
    page.click_send_button()
    page.check_successful_add_message()
    page.click_successful_add_message_ok_button()
    page.check_disappearing_successful_add_message()
    page.check_email_in_table(email, 1)
    page.check_name_in_table(name, 1)
    page.check_gender_in_table(gender, 1)
    page.check_choice_1_with_1_selected_options("Нет", 1)
    page.check_choice_2("2.2", 1)


# добавленная запись видна в таблице
# оба чекбокса не выбраны
def test_user_can_see_added_data_in_table_without_checkboxes(browser, setup):
    page = setup
    email = "123@mail.ru"
    name = "name"
    web_elements = page.get_genders_in_selectbox()
    genders = [el.text for el in web_elements]
    gender = genders[0]
    page.fill_email_input(email)
    page.fill_name_input(name)
    page.select_gender(gender)
    page.click_send_button()
    page.check_successful_add_message()
    page.click_successful_add_message_ok_button()
    page.check_disappearing_successful_add_message()
    page.check_email_in_table(email, 1)
    page.check_name_in_table(name, 1)
    page.check_gender_in_table(gender, 1)
    page.check_choice_1_with_1_selected_options("Нет", 1)
    page.check_choice_2("", 1)


# неуспешное добавление
# появление сообщения о неверном формате почты
def test_user_cant_add_data_with_incorrect_email_format(browser, setup):
    page = setup
    page.fill_email_input("12345")
    page.fill_name_input("name")
    web_elements = page.get_genders_in_selectbox()
    genders = [el.text for el in web_elements]
    gender = genders[0]
    page.select_gender(gender)
    page.click_send_button()
    page.check_wrong_email_format_message()


# неуспешное добавление
# появление сообщения о незаполненном поле "имя"
def test_user_cant_add_data_with_empty_name_input(browser, setup):
    page = setup
    page.fill_email_input("123@mail.ru")
    page.fill_name_input("")
    web_elements = page.get_genders_in_selectbox()
    genders = [el.text for el in web_elements]
    gender = genders[0]
    page.select_gender(gender)
    page.click_send_button()
    page.check_wrong_empty_name_input_message()


# возможность закрыть сообщение о неверном формате почты
def test_user_can_close_wrong_email_format_message(browser, setup):
    page = setup
    page.fill_email_input("12345")
    page.fill_name_input("name")
    web_elements = page.get_genders_in_selectbox()
    genders = [el.text for el in web_elements]
    gender = genders[0]
    page.select_gender(gender)
    page.click_send_button()
    page.check_wrong_email_format_message()
    page.close_message()
    page.check_disappearing_wrong_email_format_message()


# возможность закрыть сообщение о незаполненном поле "имя"
def test_user_can_close_empty_name_input_message(browser, setup):
    page = setup
    page.fill_email_input("123@mail.ru")
    page.fill_name_input("")
    web_elements = page.get_genders_in_selectbox()
    genders = [el.text for el in web_elements]
    gender = genders[0]
    page.select_gender(gender)
    page.click_send_button()
    page.check_wrong_empty_name_input_message()
    page.close_message()
    page.check_disappearing_empty_name_input_message()


# неуспешное добавление с пустыми данными
def test_user_cant_add_empty_data(browser, setup):
    page = setup
    page.click_send_button()
    page.check_wrong_email_format_message()


# неуспешное добавление данных с только пробелами
def test_user_cant_add_spaces_data(browser, setup):
    page = setup
    page.fill_email_input(" ")
    page.fill_name_input(" ")
    page.click_send_button()
    page.check_wrong_email_format_message()


# успешное добавление данных с пробелами в начале
# проверка, что в таблице пробелы в начале убраны
def test_user_cant_add_spaces_before_data(browser, setup):
    page = setup
    email_with_spaces = "    123@mail.ru"
    name_with_spaces = "    name"
    web_elements = page.get_genders_in_selectbox()
    genders = [el.text for el in web_elements]
    gender = genders[0]
    page.fill_email_input(email_with_spaces)
    page.fill_name_input(name_with_spaces)
    page.select_gender(gender)
    page.click_send_button()
    page.check_successful_add_message()
    page.click_successful_add_message_ok_button()
    page.check_disappearing_successful_add_message()
    page.check_email_in_table(email_with_spaces.lstrip(), 1)
    page.check_name_in_table(name_with_spaces.lstrip(), 1)
    page.check_gender_in_table(gender, 1)
    page.check_choice_1_with_1_selected_options("Нет", 1)
    page.check_choice_2("", 1)