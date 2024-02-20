from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chromium.service import ChromiumService
from pages.home_page import HomePage


class TestCarPage:
    def setup_method(self, method):
        self.driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://guest:welcome2qauto@qauto.forstudy.space/")

    def teardown_method(self, method):
        self.driver.quit()

    def test_page_load(self):
        page = HomePage(self.driver)
        assert page.check_if_loaded() is True

    def test_login_user(self):
        page = HomePage(self.driver)
        loginpage = page.click_sign_in_button()
        garagepage = loginpage.login_with_valid_user("createduser")
        carpage = garagepage.click_add_car_button()
        carpage.enter_mileages('1000')
        carpage.click_add()
        expensespage = garagepage.click_add_expenses_button()
        expensespage.enter_number_of_liters("1000")
        expensespage.enter_total_cost("2000")
        expensespage.click_add()

