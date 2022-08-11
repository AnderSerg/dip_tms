from selenium.webdriver.common.by import By


class RegionalSettingsPage:
    country_loc = (By.ID, "select2-country_code-au-container")
    currency_loc = (By.NAME, "currency_code")

# for git
