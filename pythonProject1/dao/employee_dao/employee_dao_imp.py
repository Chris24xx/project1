from dao.employee_dao.employee_dao_ab import EmployeeAb
from entities.employee import Employee
from util.db import connection


class EmployeeDaoImp(EmployeeAb):

    def create_requests(self, request: int, response: str, employee_id, manager_id):
        sql = "insert into reimbursement values(%s,%s,null,%s,default,null,%s) returning request_id"
        cur = connection.cursor()
        cur.execute(sql, (request, response, employee_id, manager_id))
        connection.commit()
        request_id = cur.fetchone()[0]
        return request_id

    def get_all_request_employee(self, employee_id) -> list:
        sql = "select requests, status from reimbursement where employee_id = %s"
        cur = connection.cursor()
        cur.execute(sql, [employee_id])
        request_records = cur.fetchall()
        request_list = []
        for requests in request_records:
            request_list.append(requests)
        return request_list

    def get_employee_info(self) -> list[Employee]:
        sql = "select * from employee"
        c = connection.cursor()
        c.execute(sql)
        employee_record = c.fetchall()
        employee_list = []
        for employee in employee_record:
            employee_list.append(Employee(*employee))
        return employee_list

    def employee_get_request_by_id(self, request_id):
        sql = "select requests, status, managers_comment from reimbursement where request_id = %s"
        cur = connection.cursor()
        cur.execute(sql, [request_id])
        request = cur.fetchone()
        return request
