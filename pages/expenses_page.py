from pages.base_page import BasePage
from utils.locators import expensesPageLocators

class ExpensesPage(BasePage):
    def __init__(self, driver):
        self.locator = expensesPageLocators
        super().__init__(driver=driver)

    def enter_number_of_liters(self, numberofliters):
        self.find_element(*self.locator.NUMBEROFLITERSFIELD).send_keys(numberofliters)

    def enter_total_cost(self, totalcost):
        self.find_element(*self.locator.TOTALCOSTFIELD).send_keys(totalcost)

    def click_add(self):
        self.find_element(*self.locator.ADDBUTTON).click()

    def click_cancel(self):
        self.find_element(*self.locator.CANCELBUTTON).click()

    def click_close(self):
        self.find_element(*self.locator.CROSSICON).click()
