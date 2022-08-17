import time
from selenium.webdriver.common.by import By
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

    # def add_one_duck(self):
    #     add_duck_btn = self.chrome.find_element(*DuckLoc.LOCATOR_ADD_TO_CART)
    #     add_duck_btn.click()
    #     time.sleep(3)

    def add_one_duck(self):
        if self.chrome.find_element(By.XPATH, '//*[@id="box-product"]/div[1]/h1').text == "Yellow Duck":
            duck_page = self.chrome.find_element(By.XPATH, '//*[@id="box-product"]/div[2]/div[2]/div['
                                                           '5]/form/table/tbody/tr[1]/td/select')
            duck_page.click()
            time.sleep(1)
            duck_page = self.chrome.find_element(By.XPATH, '//*[@id="box-product"]/div[2]/div[2]/div['
                                                           '5]/form/table/tbody/tr[1]/td/select/option[2]')
            duck_page.click()
            time.sleep(1)
            add_duck_btn = self.chrome.find_element(*DuckLoc.LOCATOR_ADD_TO_CART)
            add_duck_btn.click()
            time.sleep(3)
        else:
            add_duck_btn = self.chrome.find_element(*DuckLoc.LOCATOR_ADD_TO_CART)
            add_duck_btn.click()
            time.sleep(3)
