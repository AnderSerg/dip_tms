import time
from Pages.base_page import BasePage
from Locators.main_page_loc import MainPageLoc
from Locators.main_page_loc import LoginLoc


class MainPage(BasePage):
    locator = ''

    def go_to_regional_settings(self):
        time.sleep(1)
        regional_settings = self.chrome.find_element(*MainPageLoc.LOCATOR_REGIONAL_SETTINGS)
        regional_settings.click()

    def currency_check(self):
        usd_eur = self.chrome.find_element(*MainPageLoc.LOCATOR_CURRENCY_MAIN).text
        assert usd_eur == 'EUR'
        time.sleep(1)

    def country_check(self):
        country = self.chrome.find_element(*MainPageLoc.LOCATOR_COUNTRY_MAIN).text
        assert country == 'Belarus'
        time.sleep(1)

    ####################################################################################################

    def login_user(self):
        email = self.chrome.find_element(*LoginLoc.LOCATOR_EMAIL)
        email.send_keys('email@mail.ru')
        time.sleep(2)

        passwd = self.chrome.find_element(*LoginLoc.LOCATOR_PASSWORD)
        passwd.send_keys('user')
        time.sleep(2)

        btn_login = self.chrome.find_element(*LoginLoc.LOCATOR_LOGIN_BTN)
        btn_login.click()
        time.sleep(2)

    def go_to_duck_page(self):
        duck_page = self.chrome.find_element(*MainPageLoc.LOCATOR_DUCK_PAGE)
        duck_page.click()

    def go_to_edit_account_page(self):
        account_page = self.chrome.find_element(*MainPageLoc.LOCATOR_EDIT_ACCOUNT)
        account_page.click()
