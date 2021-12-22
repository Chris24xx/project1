import time

from behave import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.alert import Alert


@given(u'Employee is on the Employee Home page')
def step_impl(context):
    context.driver.get(
        "file:///C:/Users/Latin/OneDrive/Desktop/Revature/pythonProject1/web_pages/employee_home_page.html")


@when(u'Employee inputs 200 into the amount box')
def step_impl(context):
    context.project1.input_amount().send_keys("200")


@when(u'Employee inputs 1 into the first employee box')
def step_impl(context):
    context.project1.Input_id().send_keys('1')


@when(u'Employee inputs travel into the reason box')
def step_impl(context):
    context.project1.input_reason().send_keys("travel")


@when(u'Employee inputs 1 into the manager box')
def step_impl(context):
    context.project1.input_man_id().send_keys('1')


@when(u'Employee clicks on the submit button on Employee Home Page')
def step_impl(context):
    context.project1.create_requests_button().click()


@then(u'an alert is given')
def step_impl(context):
    alert = Alert(context.driver)
    assert alert
