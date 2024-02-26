import time

import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from Locators.duck_page_loc import DuckLoc
from Pages.cart_page import CartPage
from Pages.duck_page import DuckPage
from Pages.main_page import MainPage
from Pages.regional_settings_page import RegionalSettingsPage
from Pages.edit_account_page import EditAccountPage

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


@allure.story("Test login - mail: email@mail.ru; password: user. Go to edit account page")
def test_login(open_browser):
    link = "http://localhost/litecart/en/"
    main_page = MainPage(open_browser, link)
    main_page.open()
    with allure.step("Check login"):
        main_page.login_user()

    main_page.go_to_edit_account_page()


@allure.story("Change and save First name: user2")
def test_duck(open_browser):
    link = "http://localhost/litecart/en/"
    main_page = MainPage(open_browser, link)
    main_page.open()
    main_page.login_user()
    main_page.go_to_edit_account_page()

    edit_account_test = EditAccountPage(open_browser, open_browser.current_url)
    with allure.step("Change login"):
        edit_account_test.change_username()
    with allure.step("Save Change login"):
        edit_account_test.save_change_username()


@allure.story("Check username in base")
def test_sql():
    db = mysql.connect(
        host="localhost",
        user="root",
        passwd="",
        database="litecart",
        port=3307
    )

    cursor = db.cursor()

    query = "SELECT firstname FROM lc_customers ORDER BY firstname DESC LIMIT 1"
    cursor.execute(query)
    print(cursor.fetchall())

    db.close()


@allure.story("Add one duck")
def test_add_one_duck(open_browser):
    link = "http://localhost/litecart/en/"
    main_page = MainPage(open_browser, link)
    main_page.open()

    main_page.go_to_duck_page()

    duck_page_test = DuckPage(open_browser, open_browser.current_url)
    duck_page_test.add_duck()


@allure.story("Go to cart")
def test_go_to_cart_func(open_browser):
    link = "http://localhost/litecart/en/"
    main_page = MainPage(open_browser, link)
    main_page.open()

    main_page.go_to_duck_page()

    duck_page_test = DuckPage(open_browser, open_browser.current_url)
    duck_page_test.add_duck()
    duck_page_test.go_to_cart()


@allure.story("Change Number of Ducks and Update")
def test_cart_and_confirm(open_browser):
    link = "http://localhost/litecart/en/"
    main_page = MainPage(open_browser, link)
    main_page.open()

    main_page.go_to_duck_page()

    duck_page_test = DuckPage(open_browser, open_browser.current_url)
    duck_page_test.add_duck()
    duck_page_test.go_to_cart()
    cart_page_test = CartPage(open_browser, open_browser.current_url)

    with allure.step("change number of ducks"):
        cart_page_test.change_number_of_ducks()
    with allure.step("Update number of ducks"):
        cart_page_test.update_number_of_ducks()


@allure.story("Check price ducks")
def test_numer_and_price_of_ducks(open_browser):
    link = "http://localhost/litecart/en/"
    main_page = MainPage(open_browser, link)
    main_page.open()

    main_page.go_to_duck_page()

    duck_page_test = DuckPage(open_browser, open_browser.current_url)
    duck_page_test.add_3_duck()
    duck_page_test.add_duck()
    duck_page_test.go_to_cart()
    cart_page_test = CartPage(open_browser, open_browser.current_url)

    # with allure.step("change number of ducks"):
    #     cart_page_test.change_number_of_ducks()
    #     time.sleep(3)
    # with allure.step("Update number of ducks"):
    #     cart_page_test.update_number_of_ducks()
    #     time.sleep(3)

    cart_page_test.price_duck()


@allure.story("Remove ducks from cart")
def test_remove_ducks(open_browser):
    link = "http://localhost/litecart/en/"
    main_page = MainPage(open_browser, link)
    main_page.open()

    main_page.go_to_duck_page()

    duck_page_test = DuckPage(open_browser, open_browser.current_url)

    duck_page_test.add_3_duck()
    duck_page_test.add_duck()
    duck_page_test.go_to_cart()
    cart_page_test = CartPage(open_browser, open_browser.current_url)
    time.sleep(3)
    # with allure.step("change number of ducks"):
    #     cart_page_test.change_number_of_ducks()
    #     time.sleep(3)
    # with allure.step("Update number of ducks"):
    #     cart_page_test.update_number_of_ducks()
    #     time.sleep(3)

    cart_page_test.price_duck()

    cart_page_test.remove_ducks()


@allure.story("Check empty cart")
def test_check_empty_cart(open_browser):
    link = "http://localhost/litecart/en/"
    main_page = MainPage(open_browser, link)
    main_page.open()

    main_page.go_to_duck_page()

    duck_page_test = DuckPage(open_browser, open_browser.current_url)
    duck_page_test.add_3_duck()
    duck_page_test.add_duck()
    duck_page_test.go_to_cart()
    cart_page_test = CartPage(open_browser, open_browser.current_url)

    # with allure.step("change number of ducks"):
    #     cart_page_test.change_number_of_ducks()
    # with allure.step("Update number of ducks"):
    #     cart_page_test.update_number_of_ducks()

    cart_page_test.price_duck()

    cart_page_test.remove_ducks()

    cart_page_test.empty_cart()
