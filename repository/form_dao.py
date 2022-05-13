from abc import abstractmethod, ABC


class FormDAO(ABC):
    @abstractmethod
    def create_form(self, form_id):
        pass

    @abstractmethod
    def get_form_by_employee(self, employee_id):
        pass

    @abstractmethod
    def get_form_by_id(self, form_id):
        pass

    @abstractmethod
    def get_nonapproved_forms(self, form_id):
        pass

    @abstractmethod
    def update_form(self, change):
        pass

    @abstractmethod
    def delete_form(self, form_id):
        pass

    @abstractmethod
    def all_forms(self):
        pass
