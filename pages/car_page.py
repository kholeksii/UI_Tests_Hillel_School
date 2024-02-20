from pages.base_page import BasePage
from utils.locators import carPageLocators
from selenium.webdriver.support.ui import Select


class CarPage(BasePage):
    def __init__(self, driver):
        self.locator = carPageLocators
        super().__init__(driver=driver)

    def enter_mileages(self, mileages):
        self.find_element(*self.locator.MILEAGEFIELD).send_keys(mileages)

    def click_add(self):
        self.find_element(*self.locator.ADDBUTTON).click()

    def click_cancel(self):
        self.find_element(*self.locator.CANCELBUTTON).click()

    def click_close(self):
        self.find_element(*self.locator.CROSSICON).click()
