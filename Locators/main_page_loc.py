from selenium.webdriver.common.by import By


class MainPageLoc:
    regional_settings_loc = (By.XPATH, '//a[@href="http://localhost/litecart/en/regional_settings"]')
    country_main_page_loc = (By.CLASS_NAME, "country")
    currency_main_page_loc = (By.CLASS_NAME, "currency")
