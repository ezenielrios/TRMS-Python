from abc import abstractmethod, ABC


class EmployeeDAO(ABC):

    @abstractmethod
    def all_employees(self):
        pass

    @abstractmethod
    def get_employee_by_id(self, employee_id):
        pass

    @abstractmethod
    def update_reimbursement(self, employee_id, cost):
        pass

    @abstractmethod
    def get_username_password(self, username, password):
        pass
