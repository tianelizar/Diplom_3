from selenium.webdriver.common.by import By

class LoginLocators:
    INPUT_EMAIL = (By.CSS_SELECTOR, "input.input__textfield.text_type_main-default[name='name']")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "input.input__textfield.text_type_main-default[name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")

