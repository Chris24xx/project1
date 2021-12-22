from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class Project1:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def input_username(self):
        element: WebElement = self.driver.find_element(By.ID, "usernameInput")
        return element

    def input_password(self):
        element: WebElement = self.driver.find_element(By.ID, "passwordInput")
        return element

    def click_button(self):
        element: WebElement = self.driver.find_element(By.ID, "loginButton")
        return element

    def input_amount(self):
        element: WebElement = self.driver.find_element(By.ID, "amount")
        return element

    def Input_id(self):
        element: WebElement = self.driver.find_element(By.ID, "e-id")
        return element

    def input_reason(self):
        element: WebElement = self.driver.find_element(By.ID, "r")
        return element

    def input_man_id(self):
        element: WebElement = self.driver.find_element(By.ID, "m-id")
        return element

    def input_get_all_employee_id(self):
        element: WebElement = self.driver.find_element(By.ID, "id-2")
        return element

    def create_requests_button(self):
        element: WebElement = self.driver.find_element(By.ID, 'info')
        return element

    def alert(self):
        element: WebElement = self.driver.find_element(By.LINK_TEXT, "success")
        return element

    def find_list(self):
        element: WebElement = self.driver.find_element(By.TAG_NAME, "li")
        return element

    def click_employee_list_button(self):
        element: WebElement = self.driver.find_element(By.XPATH, '//*[@id="view"]/input[2]')
        return element

    def pending_manager_id_field(self):
        element: WebElement = self.driver.find_element(By.ID, "id-2")
        return element

    def pending_manager_id_button(self):
        element: WebElement = self.driver.find_element(By.XPATH, '/html/body/div[1]/input[2]')
        return element

    def pending_requests_list(self):
        element: WebElement = self.driver.find_element(By.XPATH, '//*[@id="requests"]/li[1]')
        return element

    def all_id_field(self):
        element: WebElement = self.driver.find_element(By.ID, "m-id3")
        return element

    def all_button(self):
        element: WebElement = self.driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > input["
                                                                        "type=submit]:nth-child(4)")
        return element

    def all_manager_list(self):
        element: WebElement = self.driver.find_element(By.CSS_SELECTOR, "#all_requests > li:nth-child(2)")
        return element

    def stat_manager_id_field(self):
        element: WebElement = self.driver.find_element(By.ID, "m-id4")
        return element

    def stat_select_button(self):
        element: WebElement = self.driver.find_element(By.CSS_SELECTOR, "#selectChoice5")
        return element

    def stat_button_submit(self):
        element: WebElement = self.driver.find_element(By.CSS_SELECTOR, 'body > div:nth-child(4) > input[type=submit]:nth-child(11)')
        return element

    def return_info(self):
        element: WebElement = self.driver.find_element(By.ID, 'returnedInfo')
        return element

    def update_comment(self):
        element: WebElement = self.driver.find_element(By.ID, "comment")
        return element

    def update_status(self):
        element: WebElement = self.driver.find_element(By.ID, "status")
        return element

    def update_requests_id(self):
        element: WebElement = self.driver.find_element(By.ID, "r-id")
        return element

    def update_submit(self):
        element: WebElement = self.driver.find_element(By.XPATH, '/html/body/div[6]/input[4]')
        return element
