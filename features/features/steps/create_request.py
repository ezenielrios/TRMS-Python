from time import sleep

from behave import given, when, then
from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver

from features.features.pages.create_request import CreateRequestPage


@given('The User is on the Create Form Page')
def get_to_create_page(context):
    driver: WebDriver = context.driver
    driver.get('C:\\Users\Ezeniel\OneDrive\Desktop\TRMSTuition-Reimbursement-Management-System\web\create_request.html')


@when('The User types {date} in the date input')
def type_into_date(context, date):
    create_request: CreateRequestPage = context.create_request_page
    create_request.date().send_keys(date)


@when('The User types {time} in the time input')
def type_into_time(context, time):
    create_request: CreateRequestPage = context.create_request_page
    create_request.time().send_keys(time)


@when('The User types {location} in the location input')
def type_into_location(context, location):
    create_request: CreateRequestPage = context.create_request_page
    create_request.location().send_keys(location)


@when('The User types {description} in the course description input')
def type_into_desc(context, description):
    create_request: CreateRequestPage = context.create_request_page
    create_request.description().send_keys(description)


@when('The User types {cost} in the cost input')
def type_into_cost(context, cost):
    create_request: CreateRequestPage = context.create_request_page
    create_request.cost().send_keys(cost)


@when('The User types {grade} in the grade input')
def type_into_grade(context, grade):
    create_request: CreateRequestPage = context.create_request_page
    create_request.grade().send_keys(grade)


@when('The User types {event} in the event input')
def type_into_event(context, event):
    create_request: CreateRequestPage = context.create_request_page
    create_request.event().send_keys(Keys.ARROW_DOWN)


@when('The User types {justification} in the justification input')
def type_into_justification(context, justification):
    create_request: CreateRequestPage = context.create_request_page
    create_request.justification().send_keys(justification)
    sleep(5)


@when('The User Clicks the Submit Button')
def click_submit(context):
    create_request: CreateRequestPage = context.create_request_page
    create_request.form_submit().click()
    sleep(5)


@then('Form should be added successfully')
def request_added(context):
    create_request: CreateRequestPage = context.create_request_page
    assert create_request.message() == create_request.message()
    sleep(5)
