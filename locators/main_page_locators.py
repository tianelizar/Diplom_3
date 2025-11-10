from selenium.webdriver.common.by import By

class MainPageLocators:

    # в хэдере
    ALL_HEADER = (By.XPATH, "//nav[contains(@class, 'AppHeader_header__nav')]")
    CONSTRUCTOR_HEADER = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText') and contains(@class, 'ml-2') and text()='Конструктор']")
    FEED_HEADER = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText') and contains(@class, 'ml-2') and text()='Лента Заказов']")

    CRATER_BUN = (By.XPATH, "//a[contains(@href, '/ingredient/61c0c5a71d1f82001bdaaa6c')]") # краторная булка
    CRATER_BUN_COUNTER = (By.XPATH,
    "//a[contains(@href, '/ingredient/61c0c5a71d1f82001bdaaa6c')]//div[contains(@class, 'counter_counter')]//p[contains(@class, 'counter_counter__num')]")

    @staticmethod
    def fresh_ingredient_by_href(href_part: str):
        return (By.XPATH, f"//a[contains(@href, '{href_part}')]")

    
    ALL_INGREDIENTS = (By.CSS_SELECTOR, "a[class*='BurgerIngredient_ingredient']") # все доступные ингредиенты
    INGREDIENTS_TEXT = (By.CSS_SELECTOR, "p[class*='BurgerIngredient_ingredient__text']") # названия всех ингредиентов

    INGREDIENT_POPUP = (By.XPATH, "//div[contains(@class, 'Modal_modal__container') and .//h2[contains(text(), 'Детали ингредиента')]]") # всплывающее окно
    POPUP_CLOSE = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//button[contains(@class, 'Modal_modal__close')]") # кнопка закрытия окна

    INGREDIENT_POPUP_TEXT = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//p[contains(@class, 'text_type_main-medium')]") # название ингредиента внутри окна

    COUNTER = (By.XPATH, "//div[contains(@class, 'counter_counter')]//p[contains(@class, 'counter_counter__num')]") # счётчик ингредиента

    CONSTRUCTOR_BASKET = (By.CSS_SELECTOR, "section.BurgerConstructor_basket__29Cd7") # корзина конструктора

    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button_type_primary') and text()='Оформить заказ']") # кнопка оформить заказ

    ORDER_POPUP = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox')]//h2[contains(@class, 'Modal_modal__title') and contains(@class, 'text_type_digits-large')]") # всплывающее окно с номером заказа
    ORDER_POPUP_CLOSE = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")

    OVERLAY = (By.CSS_SELECTOR, 'div[class*="Modal_modal_overlay"]')

    OVERLAY_MAIN = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div") # оверлей ожидания
    





