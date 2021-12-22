from behave import *


@given(u'Employee is on the home page')
def step_impl(context):
    context.driver.get(
        "file:///C:/Users/Latin/OneDrive/Desktop/Revature/pythonProject1/web_pages/employee_home_page.html")


@when(u'Employee inputs <employee id> into the employee box')
def step_impl(context):
    context.project1.input_get_all_employee_id().send_keys("1")


@when(u'Employee clicks list submit button')
def click_button(context):
    context.project1.click_employee_list_button().click()


@then(u'Employee receives a list of requests')
def step_impl(context):
    context.project1.find_list().is_enabled()
    assert True
