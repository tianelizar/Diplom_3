import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from seletools.actions import drag_and_drop
from locators.main_page_locators import MainPageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    @allure.step("Подождать видимости элементов")
    def wait_for_elements(self, locator, timeout = 30):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, element_or_locator, timeout=10):
        if isinstance(element_or_locator, WebElement):
            element = element_or_locator
        else:
            element = self.wait_for_element(element_or_locator, timeout)
        return element.text
    
    @allure.step("Подождать, когда атрибут будет содержать непустое значение")
    def wait_for_non_empty_attribute(self, locator, attribute, timeout=10):
        return WebDriverWait(self.driver, timeout).until(lambda driver: driver.find_element(*locator).get_attribute(attribute) != "")

    @allure.step('Подождать пока элемент не станет невидимым')
    def wait_for_element_hide(self, locator):
        WebDriverWait(self.driver, timeout=30).until(EC.invisibility_of_element_located(locator))
        return True
    
    @allure.step('Подождать выполнения условия')
    def wait_for_condition(self, condition):
        return WebDriverWait(self.driver, timeout=10).until(condition)

    @allure.step('Перетащить элемент')
    def drag_and_drop_element(self, source, target):
        drag_and_drop(self.driver, source, target)

    @allure.step('Проверить, что адрес страницы совпадает с ожидаемым')
    def is_expected_page(self, expected_url):
        return expected_url in self.driver.current_url
    
    @allure.step('Ввести текст в поле ввода')
    def send_keys_to_input(self, locator, keys, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step('Подождать, пока элемент станет кликабельным')
    def wait_until_element_clickable(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
    
    
    @allure.step("Кликнуть на элемент")
    def click_on_element(self, element_or_locator, timeout=10):
        if isinstance(element_or_locator, WebElement):
            element = element_or_locator
        else:
            element = self.wait_until_element_clickable(element_or_locator, timeout)
        element.click()
    
    @allure.step('Подождать исчезновения оверлея')
    def page_loading_wait(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY_MAIN)

   
    @allure.step('Проверка отсутствия оверлея')
    def no_visible_overlays(self, driver, overlay_locator):
        elems = driver.find_elements(*overlay_locator)
        return not elems or all(not e.is_displayed() for e in elems)
    
    @allure.step('Кликнуть после исчезновения оверлея')
    def click_when_ready(self, target_locator, overlay_locator, timeout=15):
        wait = WebDriverWait(
            self.driver,
            timeout,
            ignored_exceptions=(StaleElementReferenceException,)
        )

        el = wait.until(EC.visibility_of_element_located(target_locator))
        ActionChains(self.driver).move_to_element(el).perform()

        wait.until(lambda d: self.no_visible_overlays(d, overlay_locator))
        wait.until(EC.element_to_be_clickable(target_locator))

        ActionChains(self.driver).move_to_element(el).click().perform()

    @allure.step('Подождать появления элементов в списке')
    def wait_for_non_empty_elements(self, locator, timeout=15):
        def condition(driver):
            elements = driver.find_elements(*locator)
            return elements if elements else False
        return WebDriverWait(self.driver, timeout).until(condition)