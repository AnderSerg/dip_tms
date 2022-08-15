from selenium.webdriver.common.by import By


class CartLoc:

    LOCATOR_PRICE_DUCK = (By.XPATH, '//*[@id="order_confirmation-wrapper"]/table/tbody/tr[2]/td[4]')
    LOCATOR_PRICE_ALL = (By.XPATH, '//*[@id="order_confirmation-wrapper"]/table/tbody/tr[2]/td[6]')

    LOCATOR_QUANTITY_DUCKS = (By.XPATH, '//*[@id="order_confirmation-wrapper"]/table/tbody/tr[2]/td[1]')

    LOCATOR_CONFIRM_BTN = (By.XPATH, '//*[@id="order_confirmation-wrapper"]/form/div[2]/p/button')
