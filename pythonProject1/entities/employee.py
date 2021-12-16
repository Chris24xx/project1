class Employee:
    def __init__(self, full_name,employee_id, username, password, ):
        self.full_name = full_name
        self.username = username
        self.password = password
        self.employee_id = employee_id

    def dictionary(self):
        return {
            "fullName": self.full_name,
            "username": self.username,
            "password": self.password,
            "employeeId": self.employee_id
        }

    def __str__(self):
        return "Employee full name is {} and username is {} password {} employee Id ()".format(self.full_name,
                                                                                               self.username,
                                                                                               self.password,
                                                                                               self.employee_id)

    def __repr__(self):
        return "Employee name {} Username {} Password {} Employee Id {}".format(self.full_name, self.username,
                                                                                self.password, self.employee_id)
