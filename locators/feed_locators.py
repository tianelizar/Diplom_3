from selenium.webdriver.common.by import By

class FeedLocators:
    ALL_COMPLETED_COUNTER = (By.XPATH, "//p[contains(text(), 'Выполнено за все время:')]/following-sibling::p[contains(@class, 'OrderFeed_number')]") # счетчик заказов за всё время
    COMPLETED_TODAY_COUNTER = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня:')]/following-sibling::p[contains(@class, 'OrderFeed_number')]") # счётчик заказов за сегодня
    IN_PROGRESS_ORDERS_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]") # заказы в работе
    IN_PROGRESS_ORDERS_ITEMS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li[contains(@class, 'text_type_digits-default')]") # номера заказов внутри списка "в работе"
    


