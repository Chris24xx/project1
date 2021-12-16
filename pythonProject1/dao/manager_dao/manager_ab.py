from abc import ABC, abstractmethod


class ManagerAb(ABC):
    # approve or deny a request and explain why
    @abstractmethod
    def change_status_and_comment(self, status, comment, request_id):
        pass

    # view all request that are pending
    @abstractmethod
    def pending_requests(self,manager_id):
        pass

    # view all past request
    @abstractmethod
    def view_all_requests(self, manager_ab):
        pass

    # login information
    @abstractmethod
    def get_login_info(self):
        pass
