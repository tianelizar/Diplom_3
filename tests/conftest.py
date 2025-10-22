import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.', '.')))

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from helpers.data import Url
from helpers.api_auth_methods import AuthMethods
from pages.user_page import LoginUser

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get(Url.MAIN_SITE)
    elif request.param == "firefox":
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)
        driver.get(Url.MAIN_SITE)
    yield driver
    driver.quit()




@pytest.fixture
def authorized_new_user(driver):
    # Создаём нового пользователя через API
    _, user_data = AuthMethods.register_new_user()
    login_payload = {
        "email": user_data["email"],
        "password": user_data["password"]
    }

    # Открываем страницу логина
    driver.get(f'{Url.MAIN_SITE}{Url.LOGIN_PAGE}')
    login_page = LoginUser(driver)
    with allure.step("Авторизация созданного пользователя через UI"):
        login_page.page_loading_wait()
        login_page.login_existing_user(login_payload["email"], login_payload["password"])

    yield driver  # тесты используют этот драйвер с авторизацией

    # После теста удаляем пользователя через API
    login_response = AuthMethods.user_login(login_payload)
    access_token = login_response.json()["accessToken"]
    delete_response = AuthMethods.delete_user(access_token)
    assert delete_response.status_code == 200

    
