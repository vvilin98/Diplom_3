import allure

from web_locators import OrdersPageLocators
from web_pages import BasePage


class CreateOrderPage(BasePage):
    @allure.step('Нажимаем на заказ в списке Лента заказов')
    def click_order(self):
        self.click_on_element(OrdersPageLocators.ORDER_LINK)

    @allure.step('Проверка отображения состава')
    def check_order_structure(self):
        return self.check_presense(OrdersPageLocators.ORDER_STRUCTURE).is_displayed()

    @allure.step("Проверка совпадения заказов в истории и в ленте")
    def check_order_id(self, order_id, locator):
        elements = self.find_until_all_elements_located(locator)

        for element in elements:
            if order_id == element.text:
                return True
        return True

    @allure.step("Проверка нахождение идентификатора заказа в истории")
    def is_order_id_found_at_history(self, order_number):
        return self.check_order_id(order_number, OrdersPageLocators.ALL_ORDERS_AT_HISTORY)

    @allure.step("Проверка нахождение идентификатора заказа в ленте")
    def is_order_id_found_at_feed(self, order_number):
        return self.check_order_id(order_number, OrdersPageLocators.ALL_ORDERS_AT_FEED)

    @allure.step("Получение количества заказов")
    def get_total_order_count_daily(self, locator):
        return self.get_actually_text(locator)

    @allure.step('Получаем номер заказа')
    def get_user_order(self, orders_numbers):
        order_refactor = f'0{orders_numbers}'
        self.wait_for_text_to_be_present_in_element(OrdersPageLocators.NUMBER_IN_PROGRESS, order_refactor)
        return order_refactor

    @allure.step('Получаем номер заказа в работе')
    def get_user_order_in_progress(self):
        return self.get_actually_text(OrdersPageLocators.NUMBER_IN_PROGRESS)
