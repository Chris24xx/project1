import time

from behave import *
from selenium.webdriver.common.alert import Alert


@given(u'Manager is on the Manager Home page')
def step_impl(context):
    context.driver.get('file:///C:/Users/Latin/OneDrive/Desktop/Revature/pythonProject1/web_pages/manager_home_page'
                       '.html')


@when(u'Manager inputs <manager id> into manager field')
def step_impl(context):
    context.project1.pending_manager_id_field().send_keys(1)


@when(u'Manager clicks the pending requests button')
def step_impl(context):
    context.project1.pending_manager_id_button().click()


@then(u'Manager receives a list of requests')
def step_impl(context):
    context.project1.pending_requests_list().is_enabled()
    assert True


@when(u'Manager inputs <manager id> into second manager field')
def step_impl(context):
    context.project1.all_id_field().send_keys(1)


@when(u'Manager clicks the all requests button')
def step_impl(context):
    context.project1.all_button().click()


@then(u'Manager receives a list of all requests')
def step_impl(context):
    context.project1.all_manager_list().is_enabled()
    assert True


@when(u'Manager inputs <manager id> into the stat box')
def step_impl(context):
    context.project1.stat_manager_id_field().send_keys(1)


@when(u'Manager selects an option')
def step_impl(context):
    context.project1.stat_select_button().click()


@when(u'Manager submits the stat data')
def step_impl(context):
    time.sleep(2)
    context.project1.stat_button_submit().click()


@then(u'Manager will receive a statistic')
def step_impl(context):
    time.sleep(2)
    result = context.project1.return_info().is_enabled()
    assert result


@when(u'Manager inputs you ask for to much into the comment field')
def step_impl(context):
    context.project1.update_comment().send_keys("you ask for to much")


@when(u'Manager inputs Denied into the status field')
def step_impl(context):
    context.project1.update_status().send_keys('Denied')


@when(u'Manger inputs 10 into the request field')
def step_impl(context):
    context.project1.update_requests_id().send_keys("10")


@when(u'Manager clicks the submit button for update requests')
def step_impl(context):
    context.project1.update_submit().click()


@then(u'Manager should get an alert')
def step_impl(context):
    time.sleep(.5)
    assert context.driver.switch_to.alert.text == "Success"
    context.driver.switch_to.alert.accept()


@when(u'Manager inputs fine stop asking into the comment field')
def step_impl(context):
    context.project1.update_comment().send_keys('fine stop asking')


@when(u'Manager inputs Approved into the status field')
def step_impl(context):
    context.project1.update_status().send_keys('Approved')


@when(u'Manger inputs 8 into the request field')
def step_impl(context):
    context.project1.update_requests_id().send_keys('8')
