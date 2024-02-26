import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_wiki_search_field():
    chrome = webdriver.Chrome()
    try:
        url = 'http://localhost/litecart/en/'
        chrome.get(url)
        chrome.maximize_window()
        # chrome.fullscreen_window()
        # var_x = chrome.find_element(By.ID, "input_value").text
        #
        # input_x = chrome.find_element(By.ID, "answer")

        usd_eur = chrome.find_element(By.CLASS_NAME, "currency")
        usd_eur.click()
        time.sleep(5)

        country = chrome.find_element(By.CLASS_NAME, "country")
        country.click()

        reg_set = chrome.find_element(By.LINK_TEXT, "Regional Settings")
        reg_set.click()
        time.sleep(5)

        cur_change = chrome.find_element(By.XPATH, '//*[@id="box-regional-settings"]/div/form/table/tbody/tr[1]/td[2]/select/option[3]')
        cur_change.click()
        time.sleep(5)

        country_change = chrome.find_element(By.CLASS_NAME, 'select2-selection__rendered')
        country_change.click()
        country_change = chrome.find_element(By.CLASS_NAME, 'select2-search__field')
        country_change.send_keys("BELARUS\n")
        time.sleep(5)

        save_btn = chrome.find_element(By.NAME, 'save')
        save_btn.click()
        time.sleep(5)

        usd_eur = chrome.find_element(By.CLASS_NAME, "currency").text
        assert usd_eur == 'EUR'
        time.sleep(5)

        country = chrome.find_element(By.CLASS_NAME, "country").text
        assert country == 'Belarus'

    finally:
        chrome.quit()
