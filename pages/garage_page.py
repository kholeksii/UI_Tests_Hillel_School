from pages.base_page import BasePage
from pages.car_page import CarPage
from pages.expenses_page import ExpensesPage
from utils.locators import garagePageLocators


class GaragePage(BasePage):
    def __init__(self, driver):
        self.locator = garagePageLocators
        super().__init__(driver=driver)

    def click_add_car_button(self):
        self.find_element(*self.locator.ADDCARBUTTON).click()
        return CarPage(self.driver)

    def click_add_expenses_button(self):
        self.find_element(*self.locator.ADDCARBUTTON).click()
        return ExpensesPage(self.driver)