from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class CreateRequestPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def date(self):
        return self.driver.find_element(by=By.ID, value='date')

    def time(self):
        return self.driver.find_element(by=By.ID, value='time')

    def location(self):
        return self.driver.find_element(by=By.ID, value='location')

    def description(self):
        return self.driver.find_element(by=By.ID, value='description')

    def cost(self):
        return self.driver.find_element(by=By.ID, value='cost')

    def grade(self):
        return self.driver.find_element(by=By.ID, value='gradingFormat')

    def event(self):
        return self.driver.find_element(by=By.ID, value='typeOfEvent')

    def justification(self):
        return self.driver.find_element(by=By.ID, value='justification')

    def form_submit(self):
        return self.driver.find_element(by=By.ID, value='createFormButton')

    def message(self):
        return self.driver.find_element(by=By.ID, value='message')
