import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_wiki_search_field():
    chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        url = 'http://localhost/litecart/en/'
        chrome.get(url)
        chrome.maximize_window()
        # chrome.fullscreen_window()
        # var_x = chrome.find_element(By.ID, "input_value").text
        #
        # input_x = chrome.find_element(By.ID, "answer")

        email = chrome.find_element(By.NAME, 'email')
        email.send_keys('email@mail.ru')
        time.sleep(2)

        passwd = chrome.find_element(By.NAME, 'password')
        passwd.send_keys('user')
        time.sleep(2)

        btn_login = chrome.find_element(By.NAME, 'login')
        btn_login.click()
        time.sleep(2)

        duck_add = chrome.find_element(By.XPATH, '//*[@id="box-most-popular"]/div/ul/li[2]/a[1]/div[2]')
        duck_add.click()
        time.sleep(2)

        add_to_cart_btn = chrome.find_element(By.NAME, 'add_cart_product')
        add_to_cart_btn.click()
        time.sleep(2)
        add_to_cart_btn.click()
        time.sleep(2)
        add_to_cart_btn.click()
        time.sleep(2)

        cart = chrome.find_element(By.ID, 'cart')
        cart.click()

        price_duck = chrome.find_element(By.CLASS_NAME, 'unit-cost')
        price_duck = price_duck[:-2]
        price_all = chrome.find_element(By.CLASS_NAME, 'sum')
        price_all = price_all[:-2]
        #print(float(price_duck)*3 == float(price_all))

        text = chrome.find_element(By.NAME, 'tax_id')
        text.send_keys(price_duck)
        time.sleep(5)


    finally:
        chrome.quit()

# for git
