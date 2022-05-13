from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from features.features.pages.create_request import CreateRequestPage
from features.features.pages.login import LoginPage


def before_all(context):
    options = Options()

    driver: WebDriver = webdriver.Chrome(
        'C://chromedriver.exe', chrome_options=options)  # chromedriver path

    login_page = LoginPage(driver)
    create_request_page = CreateRequestPage(driver)

    context.driver = driver

    context.login_page = login_page
    context.create_request_page = create_request_page
    print("started")


def after_all(context):
    context.driver.quit()
    print("ended")
