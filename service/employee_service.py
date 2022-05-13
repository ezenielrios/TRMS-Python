from repository.employee_dao_impl import EmployeeDAOImpl


class EmployeeService:
    employee_dao = EmployeeDAOImpl()

    @classmethod
    def all_employees(cls):
        return cls.employee_dao.all_employees()

    @classmethod
    def login(cls, username, password):
        return cls.employee_dao.login(username, password)

    @classmethod
    def get_employee_by_id(cls, employee_id):
        return cls.employee_dao.get_employee_by_id(employee_id)

    @classmethod
    def update_reimbursement(cls, employee_id, cost, type):
        employee = cls.get_employee_by_id(employee_id)
        print(employee.reimbursement)

        if type == "University Courses":
            cost = cost * .80
        elif type == "Seminars":
            cost = cost * .60
        elif type == "Certification Preparation Classes":
            cost = cost * .75
        elif type == "Certification":
            cost = cost * 1
        elif type == "Technical Training":
            cost = cost * .9

        print(employee.reimbursement)

        return cls.employee_dao.update_reimbursement(employee_id, employee.reimbursement - cost)

    @classmethod
    def get_username_password(cls, username, password):
        return cls.employee_dao.get_username_password(username, password)
