from abc import ABC, abstractmethod

from entities.employee import Employee


class EmployeeServiceAb(ABC):
    # validates users
    @abstractmethod
    def employee_login(self, username: Employee, password: Employee):
        pass
    # creates reimbursement requests by employees
    @abstractmethod
    def create_requests(self, request: int, reason: str, employee_id: Employee):
        pass
    # checks what is the status of the requests, has it been approved or not
    @abstractmethod
    def review_status_of_requests(self, request_id):
        pass
    # should give a list of requests which allows a user to view all requests
    @abstractmethod
    def view_past_requests(self, employee_id):
        pass
