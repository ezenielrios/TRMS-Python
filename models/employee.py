class Employee:

    def __init__(self, employee_id=0, first_name="", last_name="", username="", password="", email="", reports_to=0,
                 reimbursement=0):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.email = email
        self.reports_to = reports_to
        self.reimbursement = reimbursement

    def json(self):
        return {
            'employeeId': self.employee_id,
            'firstName': self.first_name,
            'lastName': self.last_name,
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'reportsTo': self.reports_to,
            'reimbursement': self.reimbursement
        }

    @staticmethod
    def json_parse(json):
        # employee = Employee(reimbursement=json["reimbursement"])
        employee = Employee()
        employee.employee_id = json["employeeId"]
        employee.first_name = json["firstName"]
        employee.last_name = json["lastName"]
        employee.username = json["username"]
        employee.password = json["password"]
        employee.email = json["email"]
        employee.reports_to = json["reportsTo"]
        employee.reimbursement = json["reimbursement"]

        return employee
