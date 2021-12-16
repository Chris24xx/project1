import logging
from exceptions.checked_exceptions import *
from service.service_imp.employee_service_imp import EmployeeServiceImp, EmployeeDaoImp
from service.service_imp.manager_service_imp import ManagerServiceImp, ManagerImp
from flask import jsonify, request, Flask
from entities.manager import Manager
from entities.employee import Employee

logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f"%(asctime)s %(levelname)s %(message)s")

app: Flask = Flask(__name__)
employee_dao = EmployeeDaoImp()
employee_service = EmployeeServiceImp(employee_dao)
manager_dao = ManagerImp()
manager_service = ManagerServiceImp(manager_dao)


@app.post("/project1/employee/login")
def api_employee_login():
    try:
        request_data = request.get_json()
        username = request_data["username"]
        password = request_data["password"]
        manager_service.login_validation(username, password)
        return "success"
    except IncorrectInfo as e:
        message = {"erroe": str(e)}
        return jsonify(message)


@app.post("/project1/requests/create/<employee_id>/<manager_id>")
def api_create_requests(employee_id, manager_id):
    try:
        request_data = request.get_json()
        int(employee_id)
        reason = request_data["reason"]
        requests = request_data["requests"]
        employee_service.create_requests(int(requests), reason, int(employee_id), manager_id)
        return "your request {} with your reason {} has been sent".format(requests, reason)
    except NoNegativeException as e:
        error_message = {"error": str(e)}
        return jsonify(error_message)


@app.get("/project1/requests/review_status/<request_id>")
def api_review_status_of_requests(request_id):
    status_info = employee_service.review_status_of_requests(int(request_id))
    return jsonify(status_info)
    # if status_info is True:
    #     return "Approved"
    # if status_info is False:
    #     return "Denied"
    # else:
    #     return "Pending"


@app.get("/project1/requests/all/<employee_id>")
def api_view_past_requests(employee_id):
    info = employee_service.view_past_requests(employee_id)
    list_of_requests = []
    for i in info:
        list_of_requests.append(i)
    return jsonify(list_of_requests)


@app.post("/project1/manager/login")
def login_validation():
    try:
        request_data = request.get_json()
        username = request_data["username"]
        password = request_data["password"]
        manager_service.login_validation(username, password)
        return "success"
    except IncorrectInfo as e:
        message = {"erroe": str(e)}
        return jsonify(message)


@app.patch("/project1/manager/requests/response/<request_id>")
def request_response(request_id):
    data = request.get_json()
    status = data["status"]
    comment = data["comment"]
    int(request_id)
    manager_service.request_response(status, comment, int(request_id))


@app.get("/project1/manager/requests/pending/<manager_id>")
def api_view_pending_requests(manager_id):
    info = manager_service.view_pending_requests(manager_id)
    info_list = []
    for i in info:
        info_list.append(i)
    return jsonify(info_list)


@app.get("/project1/manager/requests/all/<manager_id>")
def api_view_all_requests(manager_id):
    info = manager_service.view_all_requests(manager_id)
    info_list = []
    for i in info:
        info_list.append(i)
    return jsonify(info_list)


def display_statistic():
    data = request.get_json()
    pass

@app.get("/project1/employee/info")
def grab_employee_id():
    info = employee_service.get_employee_id()
    info_list = []
    for i in info:
        make_dict = i.employee_dictionary()
        info_list.append(make_dict)
    return jsonify(info_list)

@app.get("/project1/manager/info")
def grab_managers_id():
    info = manager_service.grab_id()
    info_list = []
    for i in info:
        make_dict = i.manager_dictionary()
        info_list.append(make_dict)
    return jsonify(info_list)


app.run()
