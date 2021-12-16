from abc import ABC, abstractmethod
from entities.employee import Employee
from entities.manager import Manager


class EmployeeAb(ABC):
    # use this method to grab the username and password to be validated against the input info
    @abstractmethod
    def get_employee_info(self) -> list[Employee]:
        pass

    # using an id we can grab the request so the employee can see if its been approve or not.
    @abstractmethod
    def employee_get_request_by_id(self, employee_id):
        pass

    @abstractmethod
    def get_all_request_employee(self, employee_id) -> list:
        pass

    @abstractmethod
    def create_requests(self, request: int, response: str, employee: Employee, manager:Manager):
        pass
