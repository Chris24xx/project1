class Manager:
    def __init__(self, full_name,username,password,manager_id):
        self.manager_id = manager_id
        self.username = username
        self.password = password
        self.full_name = full_name

    def dictionary(self):
        return{
            "fullName" : self.full_name,
            "username" : self.username,
            "password" : self.password,
            "manager_id": self.manager_id
        }
