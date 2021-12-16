from dao.employee_dao.employee_dao_imp import EmployeeDaoImp
from entities.employee import Employee
from service.service_imp.employee_service_imp import EmployeeServiceImp
from exceptions.checked_exceptions import *

employee_dao = EmployeeDaoImp()
employee_service = EmployeeServiceImp(employee_dao)


def test_service_create_requests():
    try:
        employee_service.create_requests(-1, "cause", 1)
        assert False
    except NoNegativeException as e:
        assert str(e) == "Negative Input"


def test_status():
    result = employee_service.review_status_of_requests(8)
    print(result)
    assert result


def test_employee_login():
    result: Employee = employee_service.employee_login("test", "password1")
    assert result


def test_response():
    result = employee_service.view_response(8)
    print(result)
    assert result
