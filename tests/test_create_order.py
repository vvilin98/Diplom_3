import time

import allure
import pytest

from data.urls import Urls
from web_locators import OrdersPageLocators


class TestCreateOrder:
    @allure.title('Проверка появления всплывающего окна с деталями при клике на заказ')
    @allure.description('Кликаем на заказ и проверяем, что появилось всплывающее окно с деталями')
    def test_get_order_popup(self, pages):
        pages.click_orders_list_button()
        pages.click_order()
        assert pages.check_order_structure() == True

    @allure.title('При создании заказа этот заказа отображается как и в История заказов в ЛК профиля, так и в "Ленте заказов"')
    @allure.description('Соpдаем заказа и проверяем есть ли он в ЛК в Истории заказов и есть ли этот же заказ в "Ленте заказов"')
    def test_find_order_in_list(self, pages, login):
        pages.add_filling_to_order()
        pages.click_order_button()
        pages.check_show_window_with_order_id()
        order_number = pages.get_with_order_id()
        pages.click_close_modal_order()
        pages.click_on_account()
        pages.click_order_history_button()
        is_order_id_found_at_history = pages.is_order_id_found_at_history(order_number)
        pages.click_orders_list_button()
        is_order_id_found_at_feed = pages.is_order_id_found_at_feed(order_number)
        assert is_order_id_found_at_history and is_order_id_found_at_feed, "Заказы в истории и в ленте не совпадают"

    @allure.title('При создании заказа, происходит увеличения значения счетчиков заказов "Выполнено за все время"/"Выполнено за сегодня"')
    @allure.description('Сверяем счетчик заказов "Выполнено за все время" / "Выполнено за сегодня" до создания заказа и после создания заказа '
                        'Счетчик должен увеличиться')
    @pytest.mark.parametrize('counter', [OrdersPageLocators.TOTAL_ORDER_COUNT, OrdersPageLocators.DAILY_ORDER_COUNT])
    def test_today_orders_counter(self, pages, login, counter):
        pages.click_orders_list_button()
        prev_counter_value = pages.get_total_order_count_daily(counter)
        pages.click_constructor_button()
        pages.add_filling_to_order()
        pages.click_order_button()
        pages.click_close_modal_order()
        pages.click_orders_list_button()
        current_counter_value = pages.get_total_order_count_daily(counter)
        assert current_counter_value > prev_counter_value, "Заказ не создался, counter не сработал"

    @allure.title('Проверка отображения номера заказа в разделе "В работе')
    @allure.description('Получаем номер нового заказа, и проверяем, что номер заказа появился в разделе "В работе"')
    def test_new_order_appears_in_work_list(self, pages, login):
        pages.add_filling_to_order()
        pages.click_order_button()
        order_number = pages.get_with_order_id()
        pages.click_close_modal_order()
        pages.click_orders_list_button()
        order_number_refactor = pages.get_user_order(order_number)
        order_in_progress = pages.get_user_order_in_progress()
        assert order_number_refactor == order_in_progress
