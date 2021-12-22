from behave import Given, When, Then
from selenium.webdriver.support.wait import WebDriverWait
import time

@Given(u'Employee is on the login page')
def login_page(context):
    context.driver.get("file:///C:/Users/Latin/OneDrive/Desktop/Revature/pythonProject1/web_pages/employee_login.html")


@When(u'Employee inputs test into username field')
def step_impl(context):
    context.project1.input_username().send_keys('test')


@When(u'Employee inputs password1 into password field')
def step_impl(context):
    context.project1.input_password().send_keys('password1')


@When(u'Employee clicks submit button')
def step_impl(context):
    context.project1.click_button().click()


@Then(u'Employee should be redirected to the webpage with the title Employee Home Page')
def step_impl(context):
    time.sleep(.5)
    assert context.driver.title == "Employee Home Page"


@Given(u'Manager is on the login page')
def login(context):
    context.driver.get("file:///C:/Users/Latin/OneDrive/Desktop/Revature/pythonProject1/web_pages/manager_login.html")


@When(u'Manager inputs usertest into username field')
def step_impl(context):
    context.project1.input_username().send_keys('usertest')


@When(u'Manager inputs passtest into password field')
def step_impl(context):
    context.project1.input_password().send_keys('passtest')


@When(u'Manager clicks submit button')
def click_button(context):
    context.project1.click_button().click()


@Then(u'Manager should be redirected to the webpage with the title Manager')
def step_impl(context):
    time.sleep(.5)
    assert context.driver.title == "Manager"
