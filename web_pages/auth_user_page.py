import allure

from data.user_data import PersonData
from web_locators import AuthLoginLocators, MainPageLocators
from web_pages.base_page import BasePage


class AuthUserPage(BasePage):

    @allure.step('Перейти на страницу авторизации по кнопке "Войти в аккаунт"')
    def click_personal_account_button(self):
        self.move_to_element_and_click(MainPageLocators.LOGIN_PROFILE_BUTTON)

    @allure.step('Заполняем поле "email"')
    def set_email_field(self, user_email):
        self.wait_for_element_to_be_clickable(AuthLoginLocators.EMAIL_FIELD)
        self.click_on_element(AuthLoginLocators.EMAIL_FIELD)
        self.set_text_to_element(AuthLoginLocators.EMAIL_FIELD, user_email)

    @allure.step('Заполняем поле "Пароль"')
    def set_password_field(self, user_password):
        self.click_on_element(AuthLoginLocators.PASSWORD_FIELD)
        self.set_text_to_element(AuthLoginLocators.PASSWORD_FIELD, user_password)

    @allure.step('Нажимаем кнопку «Войти»')
    def click_login_button(self):
        self.click_on_element(AuthLoginLocators.LOGIN_BUTTON_ANY_FORMS)
        self.wait_for_element_to_be_clickable(MainPageLocators.PROFILE_BUTTON)

    @allure.step('Авторизация')
    def login(self):
        self.click_personal_account_button()
        self.set_email_field(PersonData.user_login)
        self.set_password_field(PersonData.user_password)
        self.click_login_button()

    @allure.step('Проверяем переход на страницу Авторизации')
    def check_switch_on_login_page(self):
        self.wait_until_element_visibility(AuthLoginLocators.LOGIN_TEXT)
        return self.get_current_url()
