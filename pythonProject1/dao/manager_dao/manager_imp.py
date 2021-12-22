from dao.manager_dao.manager_ab import ManagerAb
from entities.manager import Manager
from util.db import connection


class ManagerImp(ManagerAb):
    def change_status_and_comment(self, status, comment, request_id):
        sql = "update reimbursement set status = %s, managers_comment = %s where request_id = %s"
        cur = connection.cursor()
        cur.execute(sql, (status, comment, request_id))
        connection.commit()
        return True

    def pending_requests(self, manager_id):
        sql = "select requests, response, request_id, employee_id from reimbursement where status is null and " \
              "manager_id = %s "
        cur = connection.cursor()
        cur.execute(sql, [manager_id])
        request_data = cur.fetchall()
        request_list = []
        for requests in request_data:
            request_list.append(requests)
        return request_list

    def view_all_requests(self, manager_id):
        sql = "select requests, status, employee_id, managers_comment from reimbursement where status is not null and " \
              "manager_id = %s "
        cur = connection.cursor()
        cur.execute(sql, [manager_id])
        request_data = cur.fetchall()
        request_list = []
        for requests in request_data:
            request_list.append(requests)
        return request_list

    def get_login_info(self):
        sql = "select * from manager"
        cur = connection.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        manager_info_list = []
        for managers in data:
            manager_info_list.append(Manager(*managers))
        return manager_info_list

    def get_request_by_Id(self, request_id):
        sql = "select * from reimbursement where request_id = %s"
        c = connection.cursor()
        c.execute(sql, [request_id])
        request = c.fetchone()
        return request

    def statistics(self, manager_id):
        sql = "select requests from reimbursement where manager_id = %s"
        c = connection.cursor()
        c.execute(sql, [manager_id])
        data = c.fetchall()
        data_list = []
        for i in data:
            data_list.append(i)
        return data_list
