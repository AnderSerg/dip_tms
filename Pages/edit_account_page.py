import time
from Pages.base_page import BasePage
from Locators.edit_account_page_loc import EditAccount


class EditAccountPage(BasePage):
    def change_username(self):
        change_username_input = self.chrome.find_element(*EditAccount.LOCATOR_FIRST_NAME_FIELD)
        change_username_input.clear()
        change_username_input.send_keys("user2")
        time.sleep(2)

    def save_change_username(self):
        save_change_btn = self.chrome.find_element(*EditAccount.LOCATOR_SAVE_BTN)
        save_change_btn.click()
