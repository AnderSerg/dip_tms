from selenium.webdriver.common.by import By


class RegionalSettingsPageLoc:
    LOCATOR_CURRENCY_CHANGE = (By.XPATH, '//*[@id="box-regional-settings"]/div/form/table/tbody/tr[1]/td['
                                        '2]/select/option[3]')

    LOCATOR_COUNTRY_CHANGE = (By.CLASS_NAME, 'select2-selection__rendered')

    LOCATOR_COUNTRY_CHANGE_FIELD = (By.CLASS_NAME, 'select2-search__field')

    LOCATOR_SAVE_BTN = (By.NAME, 'save')
