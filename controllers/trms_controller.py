from flask import jsonify, request
from models.employee import Employee
from models.form import Form
from service.employee_service import EmployeeService
from service.form_service import FormService


def route(app):

    # login employee
    @app.route("/employees/login", methods=["POST"])
    def get_username_password():
        employee = EmployeeService.login(
            request.json['username'], request.json['password'])
        if employee is None:
            return request.json, 403

        print(employee.employee_id)
        return jsonify({"id": employee.employee_id}), 200

    # get all employee
    @app.route("/employee", methods=['GET'])
    def get_all_employees():
        return jsonify(EmployeeService.all_employees()), 200

    # get employee by id
    @app.route("/employees/<employee_id>", methods=['GET'])
    def get__employee(employee_id):
        employee = EmployeeService.get_employee_by_id(int(employee_id))
        return jsonify(employee.json()), 200

    # update reimbursement
    @app.route("/employees/<employee_id>", methods=['PUT'])
    def put__employee(employee_id):
        print(request.json)
        employee = Employee.json_parse(request.json)
        employee.employee_id = int(employee_id)
        # employee = EmployeeService.update_reimbursement(employee)
        return jsonify(employee.json()), 200

    # get employee forms
    @app.route("/employees/<employee_id>/forms", methods=['GET'])
    def get_employee_form_id(employee_id):
        FormService.get_form_by_employee(int(employee_id))
        return jsonify(FormService.get_form_by_employee(employee_id)), 200

    # get employee form by ID
    @app.route("/employees/<employee_id>/forms/<form_id>", methods=['GET'])
    def get_form(employee_id, form_id):
        employee_id = EmployeeService.get_employee_by_id(int(employee_id))
        form = FormService.get_form_by_id(int(form_id))
        return jsonify(form.json()), 200

    # create form
    @app.route("/employees/<employee_id>/form", methods=['POST'])
    def post_form(employee_id):
        form = Form.json_parse(request.json)
        form.employee_id = employee_id
        form = FormService.create_form(form)
        return jsonify(form.json()), 201

    # get nonapproved
    @app.route("/forms/nonapproved", methods=['get'])
    def get_nonapproved_forms():
        return jsonify(FormService.get_nonapproved_forms()), 200

    # update approval
    @app.route("/employees/<employee_id>/form/<form_id>", methods=['PUT'])
    def put_form(employee_id, form_id):
        form = Form.json_parse(request.json)
        form.employee_id = employee_id
        form.form_id = form_id
        form = FormService.update_form(form)
        return jsonify(form.json()), 200

    # Delete a form
    @app.route("/employees/<employee_id>/forms/<form_id>", methods=['DELETE'])
    def delete_form(employee_id, form_id):
        EmployeeService.get_employee_by_id(int(employee_id))
        FormService.get_form_by_id(int(form_id))
        FormService.delete_form(int(form_id))
        return "", 205

    # all forms
    @app.route("/forms", methods=['GET'])
    def all_forms():
        return jsonify(FormService.all_forms()), 200
