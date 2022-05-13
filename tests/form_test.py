import unittest
from models.form import Form
from repository.form_dao_impl import FormDAOImpl

form_dao = FormDAOImpl()
test_form = Form(0, 0, 'June', '9:00pm', 'testloc', 'testdesc', 100,
                 'testgrade', 'testtypeveent', 'justification', 1, 'testdenied')


class FormTest(unittest.TestCase):

    def test_a_create_form(self):
        new_form = form_dao.create_form(test_form)
        assert new_form.form_id != 1

    def test_b_get_form(self):
        retrieved_form = form_dao.get_form_by_id(test_form.form_id)
        print(retrieved_form.form_id)
        print(test_form.form_id)
        assert test_form.form_id == retrieved_form.form_id

    def test_c_get_nonapproved_forms(self):
        form_dao.get_nonapproved_forms(3)
        assert test_form.is_approved == 1

    def test_d_update_form(self):
        test_form.is_approved = 1
        test_form.denied_reason = 'N/A'
        update_form = form_dao.update_form(test_form)
        assert update_form.is_approved == test_form.is_approved

    def test_e_delete_form(self):
        result = form_dao.delete_form(test_form.form_id)
        assert result == True
