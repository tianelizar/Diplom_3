import allure
import pytest
from pages.constructor_page import ConstructorPage
import time

class TestConstructorPage:
    @allure.title('переход по клику на раздел «Лента заказов»')
    def test_click_on_feed_show_feed(self, driver):
        constructor_page = ConstructorPage(driver)

        with allure.step('Дождаться загрузки страницы'):
            constructor_page.page_loading_wait()

        with allure.step('Перейти по клику на ленту заказов'):
            constructor_page.click_on_feed()

        with allure.step('Дождаться загрузки страницы'):
            constructor_page.page_loading_wait()

        with allure.step('Проверить адрес страницы ленты заказов'):
            assert constructor_page.is_feed_page(), "Не открылась лента заказов"

    @allure.title('переход по клику на раздел Конструктор')
    def test_click_on_constructor_show_main_page(self, driver):
        constructor_page = ConstructorPage(driver)

        with allure.step('Дождаться загрузки страницы'):
            constructor_page.page_loading_wait()

        with allure.step('Перейти по клику на ленту заказов'):
            constructor_page.click_on_feed()

        with allure.step('Дождаться загрузки страницы'):
            constructor_page.page_loading_wait()

        with allure.step('Перейти по клику на главную страницу конструктора'):
            constructor_page.click_on_constructor()

        with allure.step('Дождаться загрузки страницы'):
            constructor_page.page_loading_wait()

        with allure.step('Проверить адрес страницы конструктора'):
            assert constructor_page.is_main_page(), "Не на главной странице конструктора"

    @allure.title('Проверить, что по клику на элемент появляется всплывающее окно с деталями')
    def test_click_on_ingredient_show_details(self, driver):
        constructor_page = ConstructorPage(driver)

        with allure.step('Дождаться загрузки страницы'):
            constructor_page.page_loading_wait()

        with allure.step('Дождаться видимости ингредиентов'):
            constructor_page.wait_for_ingredients()

        with allure.step("Выбрать случайный ингредиент"):
            chosen_ingredient = constructor_page.get_random_ingredient()

        with allure.step('Кликнуть на выбранный ингредиент'):
            constructor_page.click_on_ingredient(chosen_ingredient)

        with allure.step('Проверить появление всплывающего окна'):
            assert constructor_page.wait_for_popup(), "Всплывающее окно с деталями не появилось"

    @allure.title('Проверить, что текст во всплывающем окне совпадает с выбранным ингредиентом')
    def test_click_on_ingredient_popup_is_correct(self, driver):
        constructor_page = ConstructorPage(driver)

        with allure.step('Дождаться загрузки страницы'):
            constructor_page.page_loading_wait()

        with allure.step('Дождаться видимости ингредиентов'):
            constructor_page.wait_for_ingredients()

        with allure.step("Выбрать случайный ингредиент"):
            chosen_ingredient = constructor_page.get_random_ingredient()

        with allure.step('Получить текст ингредиента'):
            expected_text = constructor_page.get_ingredient_text(chosen_ingredient)

        with allure.step('Кликнуть на выбранный ингредиент'):
            constructor_page.click_on_ingredient(chosen_ingredient)

        with allure.step('Дождаться появления всплывающего окна'):
            constructor_page.wait_for_popup()

        with allure.step('Получить текст во всплывающем окне'):
            popup_text = constructor_page.get_popup_text()

        with allure.step('Проверить, что текст во всплывающем окне совпадает с текстом выбранного ингредиента'):
            assert constructor_page.check_popup_matches_ingredient(popup_text, expected_text), "Текст во всплывающем окне не совпадает с текстом выбранного ингредиента"

    @allure.title('Проверить, что всплывающее окно закрывается кликом по крестику')
    def test_close_popup_successfully(self, driver):
        constructor_page = ConstructorPage(driver)

        with allure.step('Дождаться загрузки страницы'):
            constructor_page.page_loading_wait()

        with allure.step('Дождаться видимости ингредиентов'):
            constructor_page.wait_for_ingredients()

        with allure.step("Выбрать случайный ингредиент"):
            chosen_ingredient = constructor_page.get_random_ingredient()

        with allure.step('Кликнуть на выбранный ингредиент'):
            constructor_page.click_on_ingredient(chosen_ingredient)

        with allure.step('Дождаться появления всплывающего окна'):
            constructor_page.wait_for_popup()

        with allure.step('Кликнуть на кнопку закрытия окна'):
            constructor_page.close_popup()

        with allure.step('Проверить, что окно закрылось'):
            assert constructor_page.check_popup_closed(), "Всплывающее окно не закрылось кликом по крестику"

    @allure.title('Проверка увеличения счётчика булки при перетаскивании в конструктор')
    def test_ingredient_counter_increase_after_drag(self, driver):
        constructor_page = ConstructorPage(driver)

        with allure.step('Дождаться загрузки страницы '):
            constructor_page.page_loading_wait()

        with allure.step('Получить начальное значение счётчика кратерной булки'):
            initial_counter = constructor_page.get_crater_bun_counter_value()

        with allure.step('Перетащить ингредиент в конструктор'):
            constructor_page.drag_and_drop_bun()

        with allure.step("Получить новое значение счётчика булки"):
            new_counter = constructor_page.get_crater_bun_counter_value()
            
        with allure.step('Проверить, что счётчик увеличился'):
            assert new_counter > initial_counter, "Счётчик не увеличился"

   
        
        

