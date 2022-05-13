class Form:

    def __init__(self, form_id=0, employee_id=0, date="", time="", location="", description="", cost=0, grading_format="", type_event="", justification="", is_approved=True, denied_reason=""):
        self.form_id = form_id
        self.employee_id = employee_id
        self.date = date
        self.time = time
        self.location = location
        self.description = description
        self.cost = cost
        self.grading_format = grading_format
        self.type_event = type_event
        self.justification = justification
        self.is_approved = is_approved
        self.denied_reason = denied_reason

    def json(self):
        return {
            'formId': self.form_id,
            'employeeId': self.employee_id,
            'date': self.date,
            'time': self.time,
            'location': self.location,
            'description': self.description,
            'cost': self.cost,
            'gradingFormat': self.grading_format,
            'typeEvent': self.type_event,
            'justification': self.justification,
            'isApproved': self.is_approved,
            'deniedReason': self.denied_reason
        }

    @staticmethod
    def json_parse(json):
        form = Form(

            date=json["date"],
            time=json["time"],
            location=json["location"],
            description=json["description"],
            cost=json["cost"],
            grading_format=json["gradingFormat"],
            type_event=json["typeEvent"],
            justification=json["justification"],
            is_approved=json['isApproved'],
            denied_reason=json['deniedReason']
        )

        return form
