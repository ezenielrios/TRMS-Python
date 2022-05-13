from repository.form_dao import FormDAO
from util.db_connection import connection
from models.employee import Employee
from models.form import Form


class FormDAOImpl(FormDAO):

    def create_form(self, form):
        sql = "INSERT INTO form VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 1, %s) RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, (form.form_id, form.employee_id, form.date, form.time, form.location, form.description,
                             float(form.cost), form.grading_format, form.type_event, form.justification, form.denied_reason))
        connection.commit()
        record = cursor.fetchone()
        return Form(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8],
                    record[9], record[10], record[11], )

    def get_form_by_employee(self, employee_id):
        sql = "SELECT * FROM form WHERE employee_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])

        records = cursor.fetchall()

        form_list = []

        for record in records:
            form = Form(record[0], record[1], record[2], record[3], record[4], record[5],
                        record[6], record[7], record[8], record[9], record[10], record[11])

            form_list.append(form.json())

        return form_list

    def get_form_by_id(self, form_id):
        sql = "SELECT * from form WHERE form_id= %s"

        cursor = connection.cursor()
        cursor.execute(sql, [form_id])

        record = cursor.fetchone()

        return Form(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8],
                    record[9], record[10], record[11])

    def get_nonapproved_forms(self, form_id):
        sql = "SELECT * FROM form WHERE is_approved = 1"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()

        form_list = []
        for record in records:
            form = Form(record[0], record[1], record[2], record[3], record[4], record[5],
                        record[6], record[7], record[8], record[9], record[10], record[11])
            form_list.append(form.json())
        return form_list

    def update_form(self, change):
        sql = "UPDATE form SET is_approved = %s , denied_reason = %s WHERE form_id = %s RETURNING *"
        cursor = connection.cursor()
        cursor.execute(
            sql, (change.is_approved, change.denied_reason, change.form_id))
        connection.commit()
        record = cursor.fetchone()

        form = Form(record[0], record[1], record[2], record[3], record[4], record[5],
                    record[6], record[7], record[8], record[9], record[10], record[11])
        return form

    def delete_form(self, form_id):
        sql = "DELETE from form WHERE form_id= %s"

        cursor = connection.cursor()
        cursor.execute(sql, [form_id])
        connection.commit()
        return True

    def all_forms(self):

        sql = "SELECT * FROM form"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()

        form_list = []

        for record in records:
            form = Form(record[0], record[1], record[2], record[3], record[4], record[5],
                        record[6], record[7], record[8], record[9], record[10], record[11])
            form_list.append(form.json())

        return form_list
