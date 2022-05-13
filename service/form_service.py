from repository.form_dao_impl import FormDAOImpl
from models.employee import Employee
from service.employee_service import EmployeeService


class FormService:
    form_dao = FormDAOImpl()

    @classmethod
    def create_form(cls, form):
        return cls.form_dao.create_form(form)

    @classmethod
    def get_form_by_employee(cls, employee):
        return cls.form_dao.get_form_by_employee(employee)

    @classmethod
    def get_form_by_id(cls, form_id):
        return cls.form_dao.get_form_by_id(form_id)

    @classmethod
    def get_nonapproved_forms(cls):
        return cls.form_dao.get_nonapproved_forms()

    @classmethod
    def update_form(cls, form):
        EmployeeService.update_reimbursement(
            form.employee_id, form.cost, form.type_event)
        return cls.form_dao.update_form(form)

    @classmethod
    def delete_form(cls, form_id):
        return cls.form_dao.delete_form(form_id)

    @classmethod
    def all_forms(cls):
        return cls.form_dao.all_forms()
