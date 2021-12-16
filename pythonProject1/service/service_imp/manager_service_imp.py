from service.service_abstract.manager_service_abstract import ManagerServiceAb
from dao.manager_dao.manager_imp import ManagerImp
from statistics import *
from itertools import chain
from exceptions.checked_exceptions import *


class ManagerServiceImp(ManagerServiceAb):
    def __init__(self, manager_dao: ManagerImp):
        self.manager_dao = manager_dao

    def login_validation(self, username, password):
        credentials = self.manager_dao.get_login_info()
        for manager_record in credentials:
            if manager_record.username == username:
                if manager_record.password == password:
                    return True
                elif manager_record.password != password:
                    raise IncorrectInfo("Incorrect Info")
            else:
                raise IncorrectInfo("Incorrect Info")

    def request_response(self, status, comment, request_id):
        if status == "Approved":
            db_status = True
            updated_info = self.manager_dao.change_status_and_comment(db_status, comment, request_id)
            return updated_info
        if status == "Denied":
            db_status = False
            updated_info = self.manager_dao.change_status_and_comment(db_status, comment, request_id)
            return updated_info
        else:
            db_status = None
            updated_info = self.manager_dao.change_status_and_comment(db_status, comment, request_id)
            return updated_info

    def view_pending_requests(self, manager_id):
        return self.manager_dao.pending_requests(manager_id)

    def view_all_requests(self, manager_id):
        return self.manager_dao.view_all_requests(manager_id)

    def avg(self,manager_id):
        data = self.manager_dao.statistics(manager_id)
        temp = list(chain(*data))
        res = mean(temp)
        return res

    def sum(self,manager_id):
        data = self.manager_dao.statistics(manager_id)
        temp = list(chain(*data))
        res = sum(temp)
        return res

    def max(self,manager_id):
        data = self.manager_dao.statistics(manager_id)
        temp = list(chain(*data))
        res = max(*temp)
        return res

    def min(self,manager_id):
        data = self.manager_dao.statistics(manager_id)
        temp = list(chain(*data))
        res = min(*temp)
        return res

    def freq(self,manager_id):
        data = self.manager_dao.statistics(manager_id)
        temp = list(chain(*data))
        res = mode(temp)
        return res

    def display_statistics(self, stat_func, manager_id):
        return_value = stat_func(manager_id)
        return return_value

