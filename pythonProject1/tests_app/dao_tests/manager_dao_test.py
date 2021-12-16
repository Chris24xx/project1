from dao.manager_dao.manager_imp import ManagerImp

manager_dao = ManagerImp()


def test_get_all_requests():
    result = manager_dao.view_all_requests(1)
    assert len(result) >= 2


def test_get_pending_requests():
    result = manager_dao.pending_requests(1)
    assert len(result) >= 2


def test_update_requests():
    result = manager_dao.change_status_and_comment(None, "Nope", 8)
    assert result


def test_get_login_info():
    result = manager_dao.get_login_info()
    assert len(result) >= 2
