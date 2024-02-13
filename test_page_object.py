import allure
import pytest
from selenium import webdriver
from Pages.cart_page import CartPage
from Pages.duck_page import DuckPage
from Pages.main_page import MainPage
from Pages.regional_settings_page import RegionalSettingsPage

import mysql.connector as mysql


@pytest.fixture
def open_browser():
    options = webdriver.ChromeOptions()
    chrome = webdriver.Chrome(options=options)
    chrome.implicitly_wait(10)
    yield chrome
    chrome.quit()


@allure.story("Open MainPage")
def test_open_app(open_browser):
    link = "http://localhost/litecart/en/"
    main_page = MainPage(open_browser, link)
    with allure.step("Open"):
        main_page.open()


@allure.story("Change currency and country on Regional Settings page")
def test_currency_and_country_change(open_browser):
    link = "http://localhost/litecart/en/"
    main_page = MainPage(open_browser, link)
    with allure.step("Open"):
        main_page.open()
    with allure.step("Go to regional settings page"):
        main_page.go_to_regional_settings()

    reg_set_page = RegionalSettingsPage(open_browser, open_browser.current_url)
    with allure.step("Change currency"):
        reg_set_page.currency_change_on_usd()
    with allure.step("Change country"):
        reg_set_page.country_change_on_belarus()
    reg_set_page.save_changes()


@allure.story("Check changes of currency and country on main page")
def test_check_changes(open_browser):
    link = "http://localhost/litecart/en/"
    main_page = MainPage(open_browser, link)
    with allure.step("Open"):
        main_page.open()
    with allure.step("Go to regional settings page"):
        main_page.go_to_regional_settings()

    reg_set_page = RegionalSettingsPage(open_browser, open_browser.current_url)
    with allure.step("Change currency"):
        reg_set_page.currency_change_on_usd()
    with allure.step("Change country"):
        reg_set_page.country_change_on_belarus()
    with allure.step("Save changes"):
        reg_set_page.save_changes()
    with allure.step("Check currency"):
        main_page.currency_check()
    with allure.step("Check country"):
        main_page.country_check()


#####################################################################################################################

@allure.story("Test login - mail: email@mail.ru; password: user")
def test_login(open_browser):
    link = "http://localhost/litecart/en/"
    main_page = MainPage(open_browser, link)
    with allure.step("Open"):
        main_page.open()
    with allure.step("Check login"):
        main_page.login_user()


@allure.story("Test add 3 ducks in cart and go to cart")
def test_duck(open_browser):
    link = "http://localhost/litecart/en/"
    main_page = MainPage(open_browser, link)
    main_page.open()
    with allure.step("Login user"):
        main_page.login_user()
    with allure.step("Go to duck page"):
        main_page.go_to_duck_page()

    duck_page_test = DuckPage(open_browser, open_browser.current_url)
    with allure.step("Add 3 ducks"):
        duck_page_test.add_3_duck()
    with allure.step("Go to cart"):
        duck_page_test.go_to_cart()


@allure.story("Check price duck and confirm order")
def test_cart_and_confirm(open_browser):
    link = "http://localhost/litecart/en/"
    main_page = MainPage(open_browser, link)
    with allure.step("Change country"):
        main_page.open()
    with allure.step("Login user"):
        main_page.login_user()
    with allure.step("Go to duck page"):
        main_page.go_to_duck_page()

    duck_page_test = DuckPage(open_browser, open_browser.current_url)
    with allure.step("Add duck"):
        duck_page_test.add_duck()
    with allure.step("Go to cart"):
        duck_page_test.go_to_cart()

    cart_page_test = CartPage(open_browser, open_browser.current_url)
    with allure.step("Check price duck(s)"):
        cart_page_test.price_duck()
    with allure.step("Confirm order"):
        cart_page_test.confirm()


# @allure.story("Check order in base")
# def test_sql():
#     db = mysql.connect(
#         host="localhost",
#         user="root",
#         passwd="",
#         database="litecart"
#     )
#
#     cursor = db.cursor()
#
#     cursor.execute("SHOW TABLES")
#     print(cursor.fetchall())
#
#     query = "SELECT customer_lastname FROM lc_orders ORDER BY customer_lastname DESC LIMIT 1"
#     cursor.execute(query)
#     print(cursor.fetchall())
#
#     db.close()
