from django.test import SimpleTestCase

from forms_and_views_app.forms import PersonForm


# No i podstawowe testowanie formulrzy.
# Tutaj większość uwagi skupiamy na walidacji.
# Czy poprawne dane są poprawnie przekazywane
# i czy niepoprawne dane zwracają właściwe komunikaty/zachowania.
class TestForms(SimpleTestCase):
    def test_person_form_valid_data(self):
        form = PersonForm(data={"name": "Ewa", "age": 40, "city": "Warsaw"})

        self.assertTrue(form.is_valid())

    def test_person_form_no_data(self):
        form = PersonForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)

# Jeżeli chcielibyśmy przetestować frontend/ui, należy użyć odpowiedniej biblioteki.
# Najpopularniejszą biblioteką do testowania frontendu aplikacji webowych jest
# Selenium
# https://www.selenium.dev/
# tutaj znajdziesz pythonowy wrapper do selenium:
# https://pypi.org/project/selenium/
# i dokumentację do niego
# https://selenium-python.readthedocs.io/
