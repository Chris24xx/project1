from abc import ABC, abstractmethod


class ManagerServiceAb(ABC):
    @abstractmethod
    def login_validation(self,username,password):
        pass

    @abstractmethod
    def request_response(self, status, comment, request_id):
        pass

    @abstractmethod
    def view_pending_requests(self, manager_id):
        pass

    @abstractmethod
    def view_all_requests(self, manager_id):
        pass
