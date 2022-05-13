from models.employee import Employee
from repository.employee_dao import EmployeeDAO
from util.db_connection import connection


class EmployeeDAOImpl(EmployeeDAO):

    def all_employees(self):

        sql = "SELECT * FROM employee"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()

        employee_list = []

        for record in records:
            employee = Employee(record[0], record[1], record[2], record[3],
                                record[4], record[5], record[6], float(record[7]))

            employee_list.append(employee.json())

        return employee_list

    def get_employee_by_id(self, employee_id):
        sql = "SELECT * FROM employee WHERE employee_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])

        record = cursor.fetchone()

        return Employee(record[0], record[1], record[2], record[3], record[4], record[5], record[6], float(record[7]))

    def login(self, username, password):
        print(username, password)
        sql = "SELECT employee_id FROM employee WHERE username = %s AND password = %s"

        cursor = connection.cursor()
        cursor.execute(sql, [username, password])

        if cursor.rowcount == 0:
            return None

        record = cursor.fetchone()

        return Employee(record[0])

    def update_reimbursement(self, employee_id, cost):
        sql = "UPDATE employee SET reimbursement = %s WHERE employee_id = %s RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, (cost, employee_id))
        connection.commit()

        record = cursor.fetchone()

        new_employee = Employee(record[0], record[1], record[2],
                                record[3], record[4], record[5], record[6], float(record[7]))
        return new_employee

    def get_username_password(self, username, password):
        sql = "SELECT * FROM employee WHERE username=%s AND password=%s"
        cursor = connection.cursor()
        cursor.execute(sql, (username, password))

        record = cursor.fetchone()

        return Employee(record[0], record[1], record[2],
                        record[3], record[4], record[5], record[6], float(record[7]))
