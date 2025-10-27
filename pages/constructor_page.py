import allure
import random
from locators.main_page_locators import MainPageLocators
from helpers.data import Url
from pages.base_page import BasePage

class ConstructorPage(BasePage):

    @allure.step('Дождаться загрузки страницы')
    def page_loading_wait(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY_MAIN)

    @allure.step('Дождаться отображения хедера')
    def wait_for_header(self):
        self.wait_for_element(MainPageLocators.ALL_HEADER)

    @allure.step('Дождаться отображения кнопки Лента заказов')
    def wait_for_feed_button(self):
        self.wait_for_element(MainPageLocators.FEED_HEADER)

    @allure.step('Перейти по клику на ленту заказов')
    def click_on_feed(self):
        self.click_when_ready(MainPageLocators.FEED_HEADER, MainPageLocators.OVERLAY)
    
    @allure.step('Проверить адрес страницы ленты заказов')
    def is_feed_page(self):
        return self.is_expected_page(f'{Url.MAIN_SITE}{Url.ORDER_FEED}')

    @allure.step('Перейти по клику на главную страницу конструктора')
    def click_on_constructor(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_HEADER)

    @allure.step('Проверить адрес страницы конструктора')
    def is_main_page(self):
        return self.is_expected_page(Url.MAIN_SITE)

    @allure.step('Дождаться видимости ингредиентов')
    def wait_for_ingredients(self):
        return self.wait_for_elements(MainPageLocators.ALL_INGREDIENTS)

    @allure.step("Выбрать случайный ингредиент")
    def get_random_ingredient(self):
        ingredients = self.wait_for_elements(MainPageLocators.ALL_INGREDIENTS)
        return random.choice(ingredients)
    
    @allure.step('Получить текст ингредиента')
    def get_ingredient_text(self, ingredient):
        name_element = ingredient.find_element(*MainPageLocators.INGREDIENTS_TEXT)
        return self.get_text_on_element(name_element)
    

    @allure.step('Кликнуть на ингредиент')
    def click_on_ingredient(self, ingredient):
        self.click_on_element(ingredient)

    @allure.step('Проверить появление всплывающего окна')
    def wait_for_popup(self):
        return self.wait_for_element(MainPageLocators.INGREDIENT_POPUP)
    
    @allure.step('Получить текст во всплывающем окне')
    def get_popup_text(self):
        return self.get_text_on_element(MainPageLocators.INGREDIENT_POPUP)
    
    @allure.step('Проверить, что текст во всплывающем окне совпадает с текстом выбранного ингредиента')
    def check_popup_matches_ingredient(self, popup_text, expected_text):
        return expected_text in popup_text 
    
    @allure.step('Кликнуть на кнопку закрытия окна')
    def close_popup(self):
        self.click_on_element(MainPageLocators.POPUP_CLOSE)

    @allure.step('Проверить, что окно закрылось')
    def check_popup_closed(self):
        return self.wait_for_element_hide(MainPageLocators.POPUP_CLOSE)
    
    @allure.step('Перетащить ингредиент в конструктор')
    def drag_and_drop_ingredient_to_constructor(self, ingredient_element):
        constructor = self.wait_for_element(MainPageLocators.CONSTRUCTOR_BASKET)
        self.drag_and_drop_element(ingredient_element, constructor)

    @allure.step('Перетащить кратерную булку в конструктор')
    def drag_and_drop_bun(self):
        bun = self.wait_for_element(MainPageLocators.CRATER_BUN)
        self.drag_and_drop_ingredient_to_constructor(bun)

    @allure.step('Получить значение счётчика кратерной булки')
    def get_crater_bun_counter_value(self):
        counter_element = self.wait_for_element(MainPageLocators.CRATER_BUN_COUNTER)
        return int(counter_element.text)

    @allure.step('Получить значение счётчика выбранного ингредиента')
    def get_ingredient_counter_value(self, ingredient_element):
        counter_element = ingredient_element.find_element(*MainPageLocators.COUNTER)
        return int(counter_element.text)
       
    @allure.step('Нажать на Оформить заказ')
    def create_order(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON)

    @allure.step('Закрыть окно подтверждения заказа')
    def close_order_popup(self):
        self.click_on_element(MainPageLocators.ORDER_POPUP_CLOSE)

    @allure.step("Получить номер заказа")
    def get_order_number(self):
        self.wait_for_non_empty_attribute(MainPageLocators.ORDER_POPUP, "textContent", timeout=10)
        element = self.wait_for_element(MainPageLocators.ORDER_POPUP)
        return int(element.text.strip())

    @allure.step('Подождать видимости кнопки закрытия')
    def wait_popup_close_visible(self):
        self.wait_for_element(MainPageLocators.ORDER_POPUP_CLOSE)
