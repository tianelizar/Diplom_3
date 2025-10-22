import requests
import allure
from helpers.data import Url, Credentials
from helpers.generator import generate_user_data
from pages.base_page import BasePage
from locators.login_page_locators import LoginLocators
    
class LoginUser(BasePage):
    
    @allure.step('Кликнуть по полю емейл')
    def click_on_email(self):
        self.click_on_element(LoginLocators.INPUT_EMAIL)

    @allure.step('Заполнить поле емейл')
    def fill_in_email(self, email):
        self.send_keys_to_input(LoginLocators.INPUT_EMAIL, email)

    @allure.step('Кликнуть по полю пароль')
    def click_on_password(self):
        self.click_on_element(LoginLocators.INPUT_PASSWORD)
        
    @allure.step('Заполнить поле Пароль')
    def fill_in_password(self, password):
        self.send_keys_to_input(LoginLocators.INPUT_PASSWORD, password)

    @allure.step('Нажать на кнопку Войти')
    def click_on_login(self):
        self.click_on_element(LoginLocators.LOGIN_BUTTON)
    
    @allure.step('Залогиниться под существующим пользователем')
    def login_existing_user(self, email, password):
        self.click_on_email()
        self.fill_in_email(email)
        self.click_on_password
        self.fill_in_password(password)
        self.click_on_login()
