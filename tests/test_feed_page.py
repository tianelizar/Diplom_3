import allure
import pytest
from pages.feed_page import FeedPage
from pages.constructor_page import ConstructorPage

class TestFeed:

    @allure.title('Проверка увеличения счётчика заказов за всё время после создания заказа')
    def test_all_time_counter_increase_after_order(self, authorized_new_user):
        constructor_page = ConstructorPage(authorized_new_user)
        feed_page = FeedPage(authorized_new_user)

        with allure.step('Дождаться загрузки страницы'):
            constructor_page.page_loading_wait()

        with allure.step('Перейти в ленту заказов'):
            constructor_page.click_on_feed()

        with allure.step('Получить значение счётчика заказов за всё время'):
            initial_counter = feed_page.get_all_time_counter()

        with allure.step('Вернуться в конструктор'):
            constructor_page.click_on_constructor()
            constructor_page.page_loading_wait()

        with allure.step('Перетащить кратерную булку в конструктор'):
            constructor_page.wait_for_ingredients()
            constructor_page.drag_and_drop_bun()

        with allure.step('Оформить заказ'):
            constructor_page.create_order()

        with allure.step('Закрыть окно подтверждения заказа'):
            constructor_page.page_loading_wait()
            constructor_page.wait_popup_close_visible()
            constructor_page.page_loading_wait()
            constructor_page.close_order_popup()

        with allure.step('Перейти в ленту заказов'):
            constructor_page.page_loading_wait()
            constructor_page.click_on_feed()

        with allure.step('Получить новое значение счётчика заказов'):
            constructor_page.page_loading_wait()
            new_counter = feed_page.get_all_time_counter()

        with allure.step('Проверить, что значение счётчика увеличилось'):
            assert new_counter == initial_counter +1, "Значение счётчика не увеличилось"

    @allure.title('Проверить, что увеличился счётчик заказов за сегодня')
    def test_today_counter_increase_after_order(self, authorized_new_user):
        constructor_page = ConstructorPage(authorized_new_user)
        feed_page = FeedPage(authorized_new_user)

        with allure.step('Дождаться загрузки страницы'):
            constructor_page.page_loading_wait()

        with allure.step('Перейти в ленту заказов'):
            constructor_page.click_on_feed()

        with allure.step('Получить значение счётчика заказов за сегодня'):
            constructor_page.page_loading_wait()
            initial_counter = feed_page.get_today_counter()

        with allure.step('Вернуться в конструктор'):
            constructor_page.click_on_constructor()

        with allure.step('Перетащить кратерную булку в конструктор'):
            constructor_page.page_loading_wait()
            constructor_page.wait_for_ingredients()
            constructor_page.drag_and_drop_bun()

        with allure.step('Оформить заказ'):
            constructor_page.create_order()

        with allure.step('Закрыть окно подтверждения заказа'):
            constructor_page.page_loading_wait()
            constructor_page.wait_popup_close_visible()
            constructor_page.page_loading_wait()
            constructor_page.close_order_popup()

        with allure.step('Перейти в ленту заказов'):
            constructor_page.click_on_feed()

        with allure.step('Получить новое значение счётчика заказов'):
            constructor_page.page_loading_wait()
            new_counter = feed_page.get_today_counter()

        with allure.step('Проверить, что значение счётчика увеличилось'):
            assert new_counter == initial_counter +1, "Значение счётчика не увеличилось"

    @allure.title('Номер заказа появляется в разделе "В работе')
    def test_created_order_shows_in_work(self, authorized_new_user):
        constructor_page = ConstructorPage(authorized_new_user)
        feed_page = FeedPage(authorized_new_user)

        with allure.step('Дождаться загрузки страницы'):
            constructor_page.page_loading_wait()
            constructor_page.wait_for_ingredients()

        with allure.step('Перетащить кратерную булку в конструктор'):
            constructor_page.drag_and_drop_bun()

        with allure.step('Оформить заказ'):
            constructor_page.create_order()

        with allure.step('Получить номер заказа'):
            constructor_page.page_loading_wait()
            constructor_page.wait_popup_close_visible()
            constructor_page.page_loading_wait()
            order_number = constructor_page.get_order_number()

        with allure.step('Закрыть окно подтверждения заказа'):
            constructor_page.page_loading_wait()
            constructor_page.wait_popup_close_visible()
            constructor_page.page_loading_wait()
            constructor_page.close_order_popup()

        with allure.step('Перейти в ленту заказов'):
            constructor_page.page_loading_wait()
            constructor_page.click_on_feed()

        with allure.step('Получить список номеров заказов в работе'):
            order_list = feed_page.get_in_progress_orders()

        with allure.step('Проверить наличие номера заказа в списке'):
            assert order_number in order_list, "Номер заказа не появился в разделе В работе"



