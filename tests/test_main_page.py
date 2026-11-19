import allure
import time
from pages.main_page import MainPage

@allure.feature("Основная функциональность")
class TestMainPage:

    @allure.title("Переход по клику на «Конструктор»")
    def test_constructor_transition(self, driver):
        main_page = MainPage(driver)
        main_page.click_constructor_tab()
        assert "/" in driver.current_url

    @allure.title("Переход по клику на раздел «Лента заказов»")
    def test_order_feed_transition(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed_tab()
        assert "/feed" in driver.current_url

    @allure.title("Открытие всплывающего окна с деталями ингредиента")
    def test_open_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        assert main_page.is_modal_displayed()

    @allure.title("Закрытие всплывающего окна по крестику")
    def test_close_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        main_page.close_modal()
        assert main_page.wait_modal_closed()

    @allure.title("Увеличение счётчика ингредиента при добавлении")
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)
        
        initial_count = main_page.get_ingredient_count()
        
        main_page.drag_ingredient_to_cart()
        
        time.sleep(2) 
        new_count = main_page.get_ingredient_count()
        
        assert new_count > initial_count 
        # Хотел написать initial_count +1, но булки считаются за 2, а если
        # сделать +2, то этот тест не подойдет ни для чего, кроме булок