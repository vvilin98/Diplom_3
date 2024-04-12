from web_pages.auth_user_page import AuthUserPage
from web_pages.base_page import BasePage
from web_pages.main_page import MainPage
from web_pages.recovery_password_page import PasswordRecoveryPage
from web_pages.test_create_order_page import CreateOrderPage
from web_pages.user_profile_page import UserProfilePage


class UIWorkerWeb(MainPage, AuthUserPage, PasswordRecoveryPage, UserProfilePage, CreateOrderPage):
    """Класс объединяет все классы по работе со страницами используя множественно наследование"""
    def __init__(self, driver, locators):
        super().__init__(driver)
        self.locators = locators

