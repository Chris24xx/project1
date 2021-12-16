from dao.employee_dao.employee_dao_imp import EmployeeDaoImp

employee_dao = EmployeeDaoImp()


def test_get_single_request():
    result = employee_dao.employee_get_request_by_id(8)
    print(result)
    assert result


def test_get_all_requests():
    result = employee_dao.get_all_request_employee(1)
    assert len(result) >= 2


def test_get_employee_info():
    result = employee_dao.get_employee_info()
    print(result)
    assert len(result) >= 2


def test_create_request():
    result = employee_dao.create_requests(100, "new test", 1,1)
    assert result != 0
