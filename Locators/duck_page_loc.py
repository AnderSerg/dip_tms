from selenium.webdriver.common.by import By


class DuckLoc:
    LOCATOR_ADD_TO_CART = (By.NAME, 'add_cart_product')
    LOCATOR_DUCK_QUANTITY = (By.NAME, 'quantity')
    LOCATOR_GO_TO_CART = (By.ID, 'cart')
    LOCATOR_SIZE = (By.NAME, 'options[Size]')
    LOCATOR_SIZE_SMALL = (By.XPATH, '//*[@id="box-product"]/div[2]/div[2]/div[5]/form/table/tbody/tr[1]/td/select/option[2]')
