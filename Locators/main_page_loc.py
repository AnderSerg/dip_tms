from selenium.webdriver.common.by import By


class MainPageLoc:

    LOCATOR_REGIONAL_SETTINGS = (By.LINK_TEXT, "Regional Settings")
    LOCATOR_COUNTRY_MAIN = (By.CLASS_NAME, "country")
    LOCATOR_CURRENCY_MAIN = (By.CLASS_NAME, "currency")

    LOCATOR_DUCK_PAGE = (By.XPATH, '//*[@id="box-most-popular"]/div/ul/li[2]/a[1]/div[2]')


class LoginLoc:
    LOCATOR_EMAIL = (By.NAME, 'email')
    LOCATOR_PASSWORD = (By.NAME, 'password')
    LOCATOR_LOGIN_BTN = (By.NAME, 'login')