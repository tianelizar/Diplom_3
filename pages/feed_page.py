import allure
from locators.feed_locators import FeedLocators
from pages.base_page import BasePage

class FeedPage(BasePage):

    @allure.step('Получить счётчик заказов за всё время')
    def get_all_time_counter(self):
        all_counter_element = self.wait_for_element(FeedLocators.ALL_COMPLETED_COUNTER)
        all_counter_number = int(all_counter_element.text)
        return all_counter_number
    
    @allure.step('Получить счётчик заказов за сегодня')
    def get_today_counter(self):
        today_counter_element = self.wait_for_element(FeedLocators.COMPLETED_TODAY_COUNTER)
        today_counter_number = int(today_counter_element.text)
        return today_counter_number
    
    @allure.step('Получить список номеров заказов в работе')
    def get_in_progress_orders(self):
        orders_elements = self.wait_for_non_empty_elements(FeedLocators.IN_PROGRESS_ORDERS_ITEMS)
        orders_list = [int(elem.text) for elem in orders_elements]
        return orders_list


    

    

