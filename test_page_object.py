import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from Pages.cart_page import CartPage
from Pages.duck_page import DuckPage
from Pages.main_page import MainPage
from Pages.regional_settings_page import RegionalSettingsPage


@pytest.fixture
def open_browser():
    chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    chrome.implicitly_wait(10)
    yield chrome
    chrome.quit()


def test_open_app(open_browser):
    link = "http://localhost/litecart/en/"
    main_page = MainPage(open_browser, link)
    main_page.open()


def test_currency_and_country_change(open_browser):
    link = "http://localhost/litecart/en/"
    main_page = MainPage(open_browser, link)
    main_page.open()

    main_page.go_to_regional_settings()

    reg_set_page = RegionalSettingsPage(open_browser, open_browser.current_url)
    reg_set_page.currency_change_on_usd()
    reg_set_page.country_change_on_belarus()
    reg_set_page.save_changes()


def test_check_changes(open_browser):
    link = "http://localhost/litecart/en/"
    main_page = MainPage(open_browser, link)
    main_page.open()

    main_page.go_to_regional_settings()

    reg_set_page = RegionalSettingsPage(open_browser, open_browser.current_url)
    reg_set_page.currency_change_on_usd()
    reg_set_page.country_change_on_belarus()
    reg_set_page.save_changes()

    main_page.currency_check()
    main_page.country_check()

#####################################################################################################################


def test_login(open_browser):
    link = "http://localhost/litecart/en/"
    main_page = MainPage(open_browser, link)
    main_page.open()

    main_page.login_user()


def test_duck(open_browser):
    link = "http://localhost/litecart/en/"
    main_page = MainPage(open_browser, link)
    main_page.open()

    main_page.login_user()
    main_page.go_to_duck_page()

    duck_page_test = DuckPage(open_browser, open_browser.current_url)
    duck_page_test.add_duck()
    duck_page_test.go_to_cart()


def test_cart_and_confirm(open_browser):
    link = "http://localhost/litecart/en/"
    main_page = MainPage(open_browser, link)
    main_page.open()

    main_page.login_user()
    main_page.go_to_duck_page()

    duck_page_test = DuckPage(open_browser, open_browser.current_url)
    duck_page_test.add_duck()
    duck_page_test.go_to_cart()

    cart_page_test = CartPage(open_browser, open_browser.current_url)
    cart_page_test.price_duck()
    cart_page_test.confirm()
