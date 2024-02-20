from selenium.webdriver.common.by import By


class HomePageLocators(object):
    LOGO = (By.XPATH, "//a[@class='header_logo']")
    SIGNUP = (By.XPATH, "//button[text()='Sign up']")
    SIGNIN = (By.XPATH, "//button[contains(@class, 'header_signin')]")


class LoginPageLocators(object):
    EMAIL = (By.ID, "signinEmail")
    PASSWORD = (By.ID, "signinPassword")
    LOGIN = (By.CSS_SELECTOR, 'button.btn.btn-primary[type="button"]')
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'alert-danger')]")


class SignupPageLocators(object):
    NAME = (By.ID, "signupName")
    LAST_NAME = (By.ID, "signupLastName")
    EMAIL = (By.ID, "signupEmail")
    PASSWORD = (By.ID, "signupPassword")
    REPEAT_PASSWORD = (By.ID, "signupRepeatPassword")
    REGISTER = (By.XPATH, "//button[text()='Register']")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'alert-danger')]")

class carPageLocators(object):
    CARADDDIALOG = (By.CSS_SELECTOR, "app-add-car-modal")
    TITLE = (By.CSS_SELECTOR, "[class='modal-title']")
    BRANDDROPDOWN = (By.CSS_SELECTOR, "select[name='carBrandId']")
    MODELDROPDOWN = (By.CSS_SELECTOR, "select[name='carModelId']")
    MILEAGEFIELD = (By.CSS_SELECTOR, "input[name='mileage']")
    ADDBUTTON = (By.XPATH, "//button[text()='Cancel']")
    CANCELBUTTON = (By.XPATH, "//button[text()='Add']")
    CROSSICON = (By.XPATH, "//button[@class='close']")
    CAREDITDIALOG = (By.CSS_SELECTOR, "app-edit-car-modal")
    SELECTDATE = (By.CSS_SELECTOR, "input[name='carCreatedAt']")
    REMOVECARBUTTON = (By.XPATH, "//button[text()='Remove car']")

class expensesPageLocators(object):
    CARADDDIALOG = (By.CSS_SELECTOR, "app-add-expense-modal")
    TITLE = (By.CSS_SELECTOR, "[class='modal-title']")
    VEHICLEDROPDOWN = (By.ID, "addExpenseCar")
    REPORTDATEFIELD = (By.ID, "addExpenseDate")
    MILEAGEFIELD = (By.ID, "addExpenseMileage")
    NUMBEROFLITERSFIELD = (By.ID, "addExpenseLiters")
    TOTALCOSTFIELD = (By.ID, "addExpenseTotalCost")
    CANCELBUTTON = (By.XPATH, "//button[text()='Cancel']")
    ADDBUTTON = (By.XPATH, "//button[text()='Add']")
    CROSSICON = (By.XPATH, "//button[@class='close']")

class garagePageLocators(object):
    ADDCARBUTTON = (By.XPATH, "//button[text()='Add car']")
    ADDFUELEXPENSIVEBUTTON = (By.XPATH, "//button[text()='Add fuel expense']")
    EDITCARBUTTON = (By.XPATH, "//button[@class='car_edit btn btn-edit']")
    MILEAGEFIELD = (By.CSS_SELECTOR, "input[name='miles']")
    UPDATEBUTTON = (By.XPATH, "//button[text()='Update']")
