from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def username(self):
        return self.driver.find_element(by=By.ID, value='userId')

    def password(self):
        return self.driver.find_element(by=By.ID, value='userPw')

    def login_button(self):
        return self.driver.find_element(by=By.ID, value='submitBtn')
