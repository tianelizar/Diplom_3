import requests
import allure
from helpers.data import Url
from helpers.generator import generate_user_data

class AuthMethods:

    @allure.step('создание нового уникального пользователя')
    def register_new_user(self, user_data=None):
        if user_data is None:
            user_data = generate_user_data()
        response = requests.post(Url.MAIN_SITE + Url.REGISTER_API, json=user_data)
        
        return response, user_data
    
      
    @allure.step('авторизация созданного пользователя')
    def user_login(self, login_payload):
        response = requests.post(Url.MAIN_SITE+Url.LOGIN_API, json=login_payload)
        return response
    
    @allure.step('удаление пользователя')
    def delete_user(self, access_token):
        headers = {"Authorization": access_token}
        response = requests.delete(Url.MAIN_SITE + Url.USER_API, headers=headers)
        
        return response