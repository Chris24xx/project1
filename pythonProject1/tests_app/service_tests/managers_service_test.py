from service.service_imp.manager_service_imp import ManagerImp, ManagerServiceImp
from exceptions.checked_exceptions import *

manager_dao = ManagerImp()
manager_service = ManagerServiceImp(manager_dao)


def test_status_change():
    result = manager_service.request_response("Approved", "well Deserved", 9)
    assert result


def test_login():
    result = manager_service.login_validation("usertest", "passtest")
    print(result)
    assert result


def test_bad_login():
    try:
        manager_service.login_validation("bad", "bad")
        assert False
    except IncorrectInfo as e:
        assert str(e) == "Incorrect Info"


def test_bad_password():
    try:
        manager_service.login_validation("usertest", "bad")
        assert False
    except IncorrectInfo as e:
        assert str(e) == "Incorrect Info"


def test_avg():
    result = manager_service.avg()
    print(result)
    assert result


def test_sum():
    result = manager_service.sum()
    print(result)
    assert result


def test_max():
    result = manager_service.max()
    print(result)
    assert result


def test_min():
    result = manager_service.min()
    print(result)
    assert result


def test_freq():
    result = manager_service.freq()
    print(result)
    assert result


def test_display_statistic():
    result = manager_service.display_statistics(manager_service.max, 1)
    print(result)
    assert result
