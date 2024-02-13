from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Pages.base_page import BasePage
from Locators.duck_page_loc import DuckLoc


class DuckPage(BasePage):
    def add_3_duck(self):
        add_duck_quantity = self.chrome.find_element(*DuckLoc.LOCATOR_DUCK_QUANTITY)
        add_duck_quantity.clear()
        add_duck_quantity.send_keys('3')

    def go_to_cart(self):
        go_to_cart_btn = self.chrome.find_element(*DuckLoc.LOCATOR_GO_TO_CART)
        go_to_cart_btn.click()

    def add_duck(self):
        add_duck_btn = self.chrome.find_element(*DuckLoc.LOCATOR_ADD_TO_CART)
        add_duck_btn.click()
        time.sleep(1)

    def took_size(self):
        try:
            took_size_btn = self.chrome.find_element(*DuckLoc.LOCATOR_SIZE)
            took_size_btn.click()
            took_size_small = self.chrome.find_element(*DuckLoc.LOCATOR_SIZE_SMALL)
            took_size_small.select()
        except:
            Exception;
