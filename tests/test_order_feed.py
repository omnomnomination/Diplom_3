import allure
import time
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage

@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Номер заказа появляется в разделе «В работе»")
    def test_order_appears_in_progress(self, driver, registered_user):
        main_page = MainPage(driver)
        feed_page = OrderFeedPage(driver)
        
        order_number = main_page.create_order(registered_user["email"], registered_user["password"])
        
        main_page.click_order_feed_tab()
        time.sleep(3) 
        
        in_progress_orders = feed_page.get_orders_in_progress()
        
        found = False
        for number in in_progress_orders:
            if number.isdigit() and int(number) == int(order_number):
                found = True
                break
                
        assert found, f"Заказ {order_number} не найден в списке {in_progress_orders}"

    @allure.title("Счётчик «Выполнено за всё время» увеличивается при создании заказа")
    def test_total_orders_increases(self, driver, registered_user):
        main_page = MainPage(driver)
        feed_page = OrderFeedPage(driver)
        
        main_page.click_order_feed_tab()
        total_before = feed_page.get_total_orders()
        
        main_page.click_constructor_tab()
        main_page.create_order(registered_user["email"], registered_user["password"])
        
        main_page.click_order_feed_tab()
        time.sleep(3)
        
        total_after = feed_page.get_total_orders()
        assert total_after > total_before

    @allure.title("Счётчик «Выполнено за сегодня» увеличивается при создании заказа")
    def test_today_orders_increases(self, driver, registered_user):
        main_page = MainPage(driver)
        feed_page = OrderFeedPage(driver)
        
        main_page.click_order_feed_tab()
        today_before = feed_page.get_today_orders()
        
        main_page.click_constructor_tab()
        main_page.create_order(registered_user["email"], registered_user["password"])
        
        main_page.click_order_feed_tab()
        time.sleep(3)
        
        today_after = feed_page.get_today_orders()
        assert today_after > today_before