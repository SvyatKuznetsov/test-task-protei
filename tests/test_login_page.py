from pages.inputs_page import InputsPage
from pages.login_page import LoginPage


# успешная авторизация с верными данными
def test_user_can_login_with_correct_data(browser):
    link = "D:\Python\\test-task-protei-git\qa-test.html"
    page = LoginPage(browser, link)
    page.open()
    page.fill_all_inputs("test@protei.ru", "test")
    page.click_authorize_button()
    inputs_page = InputsPage(browser, browser.current_url)
    inputs_page.should_be_inputs_page()


# неуспешная авторизация с неверными данными
# появление сообщения о неверных данных
def test_user_cant_login_with_incorrect_data(browser):
    link = "D:\Python\\test-task-protei-git\qa-test.html"
    page = LoginPage(browser, link)
    page.open()
    page.fill_all_inputs("test@protei.ru", "aaaaaa")
    page.click_authorize_button()
    page.check_wrong_data_message()


# неуспешная авторизация
# появление сообщения о неверном формате почты
def test_user_cant_login_with_wrong_email_format(browser):
    link = "D:\Python\\test-task-protei-git\qa-test.html"
    page = LoginPage(browser, link)
    page.open()
    page.fill_all_inputs("test", "test")
    page.click_authorize_button()
    page.check_wrong_email_format_message()


# неуспешная авторизация
# появление сообщения о неверных данных
def test_user_can_close_wrong_data_message(browser):
    link = "D:\Python\\test-task-protei-git\qa-test.html"
    page = LoginPage(browser, link)
    page.open()
    page.fill_all_inputs("test@protei.ru", "aaaaaa")
    page.click_authorize_button()
    page.check_wrong_data_message()
    page.close_message()
    page.check_disappearing_wrong_data_message()


# возможность закрыть сообщение о неверном формате почты
def test_user_can_close_wrong_email_format_message(browser):
    link = "D:\Python\\test-task-protei-git\qa-test.html"
    page = LoginPage(browser, link)
    page.open()
    page.fill_all_inputs("test", "test")
    page.click_authorize_button()
    page.check_wrong_email_format_message()
    page.close_message()
    page.check_disappearing_wrong_email_format_message()


# неуспешная авторизация с пустыми данными
def test_user_cant_login_with_empty_data(browser):
    link = "D:\Python\\test-task-protei-git\qa-test.html"
    page = LoginPage(browser, link)
    page.open()
    page.click_authorize_button()
    page.check_wrong_email_format_message()


# неуспешная авторизация с пробелами
def test_user_cant_login_with_spaces_data(browser):
    link = "D:\Python\\test-task-protei-git\qa-test.html"
    page = LoginPage(browser, link)
    page.open()
    page.fill_all_inputs(" ", " ")
    page.click_authorize_button()
    page.check_wrong_email_format_message()


# неуспешная авторизация с пробелом перед верными данными
def test_user_cant_login_with_spaces_before_correct_data(browser):
    link = "D:\Python\\test-task-protei-git\qa-test.html"
    page = LoginPage(browser, link)
    page.open()
    page.fill_all_inputs(" test@protei.ru", " test")
    page.click_authorize_button()
    page.check_wrong_data_message()


# успешная авторизация после попытки авторизоваться с неверными данными
def test_user_can_login_after_unsuccessful_attempt(browser):
    link = "D:\Python\\test-task-protei-git\qa-test.html"
    page = LoginPage(browser, link)
    page.open()
    page.fill_all_inputs("test@protei.ru", "aaaaaa")
    page.click_authorize_button()
    page.check_wrong_data_message()
    page.close_message()
    page.check_disappearing_wrong_data_message()

    page.clear_all_inputs()
    page.fill_all_inputs("test@protei.ru", "test")
    page.click_authorize_button()
    inputs_page = InputsPage(browser, browser.current_url)
    inputs_page.should_be_inputs_page()
