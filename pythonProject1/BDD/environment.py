from behave.runner import Context
from selenium import webdriver
from BDD.page_object_model.project1_page import Project1


def before_all(context: Context):
    context.driver = webdriver.Chrome("chromedriver.exe")
    context.project1 = Project1(context.driver)
    context.driver.implicitly_wait(30)


def after_all(context):
    context.driver.quit()
