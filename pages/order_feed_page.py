from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OrderFeedPage(BasePage):
    TOTAL_ORDERS = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'OrderFeed_number')]")
    TODAY_ORDERS = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'OrderFeed_number')]")
    IN_PROGRESS_ORDERS = (By.XPATH, "//p[text()='В работе:']/following-sibling::ul/li")

    def get_total_orders(self):
        return int(self.get_text(self.TOTAL_ORDERS))

    def get_today_orders(self):
        return int(self.get_text(self.TODAY_ORDERS))

    def get_orders_in_progress(self):
        elements = self.find_elements(self.IN_PROGRESS_ORDERS)
        return [el.text for el in elements]