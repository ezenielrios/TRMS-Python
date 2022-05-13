from time import sleep
from behave import given, when, then
from selenium.webdriver.chrome.webdriver import WebDriver

from features.features.pages.login import LoginPage


@given("The User is on the Log In Page")
def login_page(context):
    driver: WebDriver = context.driver
    driver.get('C:\\login.html')#path to log in


@when('The User types test in the userId field')
def type_employee_username(context):
    login_page: LoginPage = context.login_page
    login_page.username().send_keys("test")
    sleep(3)


@when("The User types test in the userPw field")
def step_impl(context):
    login_page: LoginPage = context.login_page
    login_page.password().send_keys("test")
    # raise NotImplementedError(u'STEP: When The User types password in the password field')


@when('The User clicks on the login button')
def type_employee_log(context):
    login_page: LoginPage = context.login_page
    login_page.login_button().click()


@then('The User should be on the form Page')
def on_form(context):
    driver: WebDriver = context.driver
    driver.get('http:/form.html')#path tp form
    sleep(2)
    # assert driver.title == "Form"
