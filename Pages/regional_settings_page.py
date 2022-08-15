from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Pages.base_page import BasePage
from Locators.regional_settings_page_loc import RegionalSettingsPageLoc


class RegionalSettingsPage(BasePage):
    def currency_change_on_usd(self):
        cur_change = self.chrome.find_element(*RegionalSettingsPageLoc.LOCATOR_CURRENCY_CHANGE)
        cur_change.click()

    def country_change_on_belarus(self):
        country_change = self.chrome.find_element(*RegionalSettingsPageLoc.LOCATOR_COUNTRY_CHANGE)
        country_change.click()
        country_change = self.chrome.find_element(*RegionalSettingsPageLoc.LOCATOR_COUNTRY_CHANGE_FIELD)
        country_change.send_keys("BELARUS\n")

    def save_changes(self):
        save_btn = self.chrome.find_element(*RegionalSettingsPageLoc.LOCATOR_SAVE_BTN)
        save_btn.click()
