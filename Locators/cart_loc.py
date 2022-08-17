from selenium.webdriver.common.by import By


class CartLoc:

    LOCATOR_PRICE_DUCK = (By.XPATH, '//*[@id="order_confirmation-wrapper"]/table/tbody/tr[2]/td[4]')
    LOCATOR_PRICE_ALL = (By.XPATH, '//*[@id="order_confirmation-wrapper"]/table/tbody/tr[2]/td[6]')

    LOCATOR_QUANTITY_DUCKS = (By.XPATH, '//*[@id="order_confirmation-wrapper"]/table/tbody/tr[2]/td[1]')

    LOCATOR_CONFIRM_BTN = (By.XPATH, '//*[@id="order_confirmation-wrapper"]/form/div[2]/p/button')

    LOCATOR_ADD_DUCK_INPUT = (By.XPATH, '//*[@id="box-checkout-cart"]/div/ul/li/form/div/p[3]/input')
    LOCATOR_UPDATE_BTN_IN_CART = (By.XPATH, '//*[@id="box-checkout-cart"]/div/ul/li/form/div/p[3]/button')
    LOCATOR_REMOVE_BTN_IN_CART = (By.XPATH, '//*[@id="box-checkout-cart"]/div/ul/li/form/div/p[4]/button')

    LOCATOR_EMPTY_CART = (By.XPATH, '//*[@id="checkout-cart-wrapper"]/p[1]/em')
