from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Pages.base_page import BasePage
from Locators.cart_loc import CartLoc


class CartPage(BasePage):
    def price_duck(self):
        price_duck = self.chrome.find_element(*CartLoc.LOCATOR_PRICE_DUCK).text
        price_duck = price_duck[-2:]

        price_all = self.chrome.find_element(*CartLoc.LOCATOR_PRICE_ALL).text
        price_all = price_all[-2:]

        quantity = self.chrome.find_element(*CartLoc.LOCATOR_QUANTITY_DUCKS).text

        assert float(price_duck) * float(quantity) == float(price_all)

    def confirm(self):
        confirm_btn = self.chrome.find_element(*CartLoc.LOCATOR_CONFIRM_BTN)
        confirm_btn.click()
