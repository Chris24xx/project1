import math

from entities.employee import Employee
from service.service_abstract.employee_ab import EmployeeServiceAb
from dao.employee_dao.employee_dao_imp import EmployeeDaoImp
from exceptions.checked_exceptions import *


class EmployeeServiceImp(EmployeeServiceAb):
    def __init__(self, employee_dao: EmployeeDaoImp):
        self.employee_dao = employee_dao

    def employee_login(self, username, password):
        credentials = self.employee_dao.get_employee_info()
        for employee_record in credentials:
            if employee_record.username == username:
                if employee_record.password == password:
                    return True
                else:
                    return "incorrect information"

    def create_requests(self, request: int, reason: str, employee_id: int, manager_id):
        if request > 0:
            return self.employee_dao.create_requests(request, reason, employee_id,manager_id)
        else:
            raise NoNegativeException("Negative Input")

    def review_status_of_requests(self, request_id):
        checked_status = self.employee_dao.employee_get_request_by_id(request_id)
        if checked_status[1] is True:
            return "Approved"
        if checked_status[1] is False:
            return "Denied"
        else:
            return "Pending"

    def view_past_requests(self, employee_id):
        return self.employee_dao.get_all_request_employee(employee_id)

    def view_response(self,request_id):
        info = self.employee_dao.employee_get_request_by_id(request_id)
        return info[2]
