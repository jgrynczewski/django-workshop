from django.test import TestCase

from forms_and_views_app.models import Person


# To tak tylko przykładowo. Nie rozbudowywaliśmy modeli
# (tylko wspominaliśmy o wzorcu `fat models, skinny views`)
# więc nie ma tu za bardzo co testować.
class TestModel(TestCase):
    def setUp(self):
        self.person1 = Person.objects.create(name="Jan", age="10", city="Cracow")

    # Ale ten test nie ma sensu, bo testujemy sam model Django
    # on już jest przetesowany przez Django. Gdyby nasz model
    # robił coś nietypowego, wtedy należałoby to przetestować.
    def test_person_creation(self):
        self.assertEqual(self.person1.name, "Jan")

    # Testy modelu mają duże znaczenie kiedy stosujemy się
    # do wzorca 'fat models, skinny views'. Wszystkie umiejętności
    # modelu powinny być wtedy dobrze przetestowane.


# następny -> test_forms.py
