from selenium.webdriver.common.by import By


class EditAccount:
    LOCATOR_FIRST_NAME_FIELD = (By.NAME, 'firstname')
    LOCATOR_SAVE_BTN = (By.XPATH, '//*[@id="edit-account"]/div/form/table/tbody/tr[11]/td/button')
