from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
from pages.base_page import BasePage
from seletools.actions import drag_and_drop


class MainPage(BasePage):
    CONSTRUCTOR_TAB = (By.XPATH, "//a[@href='/']")
    ORDER_FEED_TAB = (By.XPATH, "//a[@href='/feed']")
    INGREDIENT_BUN = (By.XPATH, "//p[text()='Краторная булка N-200i']")
    
    MODAL_WINDOW = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]")
    CLOSE_MODAL_BUTTON = (By.CSS_SELECTOR, "button.Modal_modal__close__TnseK")
    INGREDIENT_COUNTER = (By.XPATH, "//a[.//p[text()='Краторная булка N-200i']]//p[contains(@class, 'counter_counter__num')]")

    CHECKOUT_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_NUMBER_IN_MODAL = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow')]")
    DROP_ZONE = (By.XPATH, "//img[@alt='Перетяните булочку сюда (низ)']")
    BUN_IN_CART = (By.XPATH, "//span[contains(@class, 'constructor-element__text') and contains(text(), 'Краторная булка N-200i')]")
    INGREDIENT_BUN_IMG = (By.XPATH, "//img[@alt='Краторная булка N-200i']")

    LOGIN_BUTTON_HEADER = (By.XPATH, "//button[text()='Войти в аккаунт']")
    EMAIL_INPUT = (By.XPATH, "//input[@type='text']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    SUBMIT_LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

    def click_constructor_tab(self):
        self.click_element(self.CONSTRUCTOR_TAB)

    def click_order_feed_tab(self):
        self.click_element(self.ORDER_FEED_TAB)

    def click_ingredient(self):
        self.click_element(self.INGREDIENT_BUN)

    def close_modal(self):
        self.click_element(self.CLOSE_MODAL_BUTTON)

    def is_modal_displayed(self):
        return self.find_element(self.MODAL_WINDOW).is_displayed()

    def wait_modal_closed(self):
        return self.wait_for_element_invisible(self.MODAL_WINDOW)

    def get_ingredient_count(self):
        return int(self.get_text(self.INGREDIENT_COUNTER))

    def login(self, email, password):
        self.click_element(self.LOGIN_BUTTON_HEADER)
        time.sleep(1)
        self.find_element(self.EMAIL_INPUT).send_keys(email)
        self.find_element(self.PASSWORD_INPUT).send_keys(password)
        self.click_element(self.SUBMIT_LOGIN_BUTTON)
        time.sleep(2)

    def drag_ingredient_to_cart(self):
        bun_img = self.find_element(self.INGREDIENT_BUN_IMG)
        target = self.find_element(self.DROP_ZONE)
        drag_and_drop(self.driver, bun_img, target)
        time.sleep(1)

    def create_order(self, email, password):
        self.login(email, password)
        
        bun = self.find_element(self.INGREDIENT_BUN_IMG) 
        target = self.find_element(self.DROP_ZONE)
        
        drag_and_drop(self.driver, bun, target)
        time.sleep(2) 
        
        self.click_element(self.CHECKOUT_BUTTON)
        time.sleep(2)
        
        order_number = self.get_text(self.ORDER_NUMBER_IN_MODAL)
        self.close_modal()
        return order_number