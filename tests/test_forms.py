from django.test import SimpleTestCase

from forms_and_views_app.forms import PersonForm


class TestForms(SimpleTestCase):
    def test_person_form_valid_data(self):
        form = PersonForm(
            data={
                'name': 'Ewa',
                'age': 40,
                'city': 'Warsaw'
            }
        )

        self.assertTrue(form.is_valid())

    def test_person_form_no_data(self):
        form = PersonForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)
