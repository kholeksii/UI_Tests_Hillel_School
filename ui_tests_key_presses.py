from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

URL = "https://the-internet.herokuapp.com/key_presses"


class TestTheInternetWebsite:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_open_url(self):
        self.driver.get(URL)
        assert self.driver.title == 'The Internet'

    def test_press_key_alphabet(self):
        self.driver.get(URL)
        assert self.driver.find_element(By.XPATH, "//div[@id='content']//h3").text == 'Key Presses'
        input_element = self.driver.find_element(By.XPATH, '//input')
        input_element.send_keys("V")
        assert self.driver.find_element(By.XPATH, "//p[@id='result']").text == 'You entered: V'

    def test_press_key_numeric(self):
        self.driver.get(URL)
        assert self.driver.find_element(By.XPATH, "//div[@id='content']//h3").text == 'Key Presses'
        input_element = self.driver.find_element(By.XPATH, '//input')
        input_element.send_keys("8")
        assert self.driver.find_element(By.XPATH, "//p[@id='result']").text == 'You entered: 8'

    def test_press_key_functional(self):
        self.driver.get(URL)
        assert self.driver.find_element(By.XPATH, "//div[@id='content']//h3").text == 'Key Presses'
        input_element = self.driver.find_element(By.XPATH, '//input')
        input_element.send_keys(Keys.CONTROL)
        assert self.driver.find_element(By.XPATH, "//p[@id='result']").text == 'You entered: CONTROL'