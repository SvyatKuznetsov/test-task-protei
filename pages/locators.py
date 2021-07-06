from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_INPUT = (By.ID, "loginEmail")
    PASS_INPUT = (By.ID, "loginPassword")
    AUTH_BUTTON = (By.ID, "authButton")
    WRONG_DATA_MESSAGE = (By.ID, "invalidEmailPassword")
    WRONG_EMAIL_FORMAT_MESSAGE = (By.ID, "emailFormatError")
    CLOSE_MESSAGE_BUTTON = (By.CSS_SELECTOR, "a.uk-alert-close.uk-close")


class InputsPageLocators:
    MAIN_FORM = (By.ID, "inputsPage")
    EMAIL_INPUT = (By.ID, "dataEmail")
    NAME_INPUT = (By.ID, "dataName")
    GENDER_SELECTBOX = (By.ID, "dataGender")
    DATA_11_CHECKBOX = (By.ID, "dataCheck11")
    DATA_12_CHECKBOX = (By.ID, "dataCheck12")
    DATA_21_RADIO_BUTTON = (By.ID, "dataSelect21")
    DATA_22_RADIO_BUTTON = (By.ID, "dataSelect22")
    DATA_23_RADIO_BUTTON = (By.ID, "dataSelect23")
    SEND_BUTTON = (By.ID, "dataSend")
    DATA_TABLE = (By.ID, "dataTable")
    SUCCESSFUL_ADD_MESSAGE = (By.CSS_SELECTOR, "div.uk-modal.uk-open")
    CLOSE_SUCCESSFUL_ADD_MESSAGE_BUTTON = (By.CSS_SELECTOR, "button.uk-button.uk-button-primary.uk-modal-close")
    NEW_ADDED_TABLE = (By.CSS_SELECTOR, "#dataTable > tbody > tr:nth-child")
    WRONG_EMAIL_FORMAT_MESSAGE = (By.ID, "emailFormatError")
    EMPTY_NAME_INPUT_MESSAGE = (By.ID, "blankNameError")
    CLOSE_MESSAGE_BUTTON = (By.CSS_SELECTOR, "a.uk-alert-close.uk-close")
