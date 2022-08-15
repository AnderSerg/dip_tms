from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Pages.base_page import BasePage
from Locators.duck_page_loc import DuckLoc


class DuckPage(BasePage):
    def add_duck(self):
        add_duck_btn = self.chrome.find_element(*DuckLoc.LOCATOR_ADD_TO_CART)
        add_duck_btn.click()
        time.sleep(1)
        add_duck_btn.click()
        time.sleep(1)
        add_duck_btn.click()
        time.sleep(1)

    def go_to_cart(self):
        go_to_cart_btn = self.chrome.find_element(*DuckLoc.LOCATOR_GO_TO_CART)
        go_to_cart_btn.click()
