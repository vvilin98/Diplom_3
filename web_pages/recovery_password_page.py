import allure
from web_locators.locators import AuthForgotPasswordlocators, AuthLoginLocators
from web_pages.base_page import BasePage


class PasswordRecoveryPage(BasePage):

    @allure.step('Нажать на "Восстановить пароль"')
    def click_password_reset_link(self):
        self.click_on_element(AuthLoginLocators.FORGOT_PASSWORD)

    @allure.step('Вводим емейл в поле для восстановления пароля')
    def set_email_for_reset_password(self, email):
        self.set_text_to_element(AuthForgotPasswordlocators.INPUT_EMAIL, email)

    @allure.step('Нажимаем на кнопку Восстановить')
    def click_reset_button(self):
        self.move_to_element_and_click(AuthForgotPasswordlocators.RESET_BUTTON)

    @allure.step('Кликаем на кнопку Показать/скрыть пароль')
    def click_on_show_password_button(self):
        self.click_on_element(AuthForgotPasswordlocators.SHOW_PASSWORD_BUTTON)

    @allure.step('Найти кнопку Сохранить')
    def find_save_button(self):
        self.wait_until_element_visibility(AuthForgotPasswordlocators.SAVE_BUTTON)

    @allure.step('Найти активное поле Пароль')
    def find_input_active(self):
        return self.wait_until_element_visibility(AuthForgotPasswordlocators.INPUT_ACTIVE)
