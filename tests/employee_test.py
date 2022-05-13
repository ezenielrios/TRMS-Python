import unittest
from models.employee import Employee
from repository.employee_dao_impl import EmployeeDAOImpl

employee_dao = EmployeeDAOImpl()

test_employee = Employee(0, 'test', 'test',
                         'test', 'test', 'test', 1, 0)


class EmployeeTest(unittest.TestCase):


    def test_get_employee_by_id(self):
        retrieved_employee = employee_dao.get_employee_by_id(
            test_employee.employee_id)
        assert test_employee.first_name == retrieved_employee.first_name


    def test_get_username_password(self):
        retrieved_employee = employee_dao.get_username_password(
            test_employee.username, test_employee.password)
        assert test_employee.username == retrieved_employee.username
        assert test_employee.password == retrieved_employee.password


if __name__ == '__main__':
    unittest.main()
