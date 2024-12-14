from django.test import TestCase
from django.urls import reverse

from forms_and_views_app.models import Person


# suita testowa
class TestViews(TestCase):

    def setUp(self):
        """Run before every single test method"""

        # To tutaj wrzucamy wszystko co chcemy, żeby zadziało się przed
        # każdym z testów jednostkowych (testami jednostkowymi nazywamy
        # metody naszej klasy, które zaczynają się prefixem `test_`. Klasę
        # nazywamy suitą testową. Po zakończeniu pojedynczego testu (metody),
        # stan bazy testowej jest czyszczony.
        self.template_view_url = reverse("forms_and_views_app:template-hello")
        self.person_detail_url = reverse("forms_and_views_app:person_detail", args=[1])
        self.create_person_url = reverse("forms_and_views_app:create_person")

        # Tworzymy wpis w bazie testowej (uwaga, po zakończeniu testu,
        # będzie on usuwany i na nowo tworzony przed rozpoczęciem kolejnego
        # testu ze suity, więc z każdym kolejnym testem sekwencja bazodanowa będzie
        # podbijała indeks naszego wpisu.
        Person.objects.create(
            name="Jan", age="11", city="Cracow"
        )  # jeżeli wpis potrzebny byłby wyłącznie na potrzebny
        # jednego testu to lepiej jego tworzenie umieścić bezpośrednio w teście

    # test jednostkowy
    def test_template_view_GET(self):

        # Tutaj pierwszy raz używamy testowego klienta. Za jego
        # pomocą możemy wysyłać proste zapytania na nasz "serwer"
        # uruchomiony w ramach testów i monitorować zwrotkę. Sam
        # obiekt zawiera w sobie znacznie więcej informacji niż
        # byśmy byli w stanie wyciągnąć z samej odpowiedzi serwera.
        # Na przykład za jego pomocą możemy zweryfikować kontekst
        # przekazany do szablonu (o czym przekonamy sie w następnym
        # teście jednostkowym.
        response = self.client.get(self.template_view_url)
        print(response)  # type: HttpResponse
        print(dir(response))

        # Tutaj sprawdzamy:
        # status odpowiedzi
        self.assertEqual(response.status_code, 200)
        # nazwę renderowanego szablonu
        self.assertTemplateUsed(response, "forms_and_views_app/hello.html")

        content = str(response.content)
        # ciało zapytania
        self.assertIn("Hello", content)

    # test jednostkowy
    def test_person_detail_GET(self):

        response = self.client.get(self.person_detail_url)

        self.assertEqual(response.status_code, 200)

        # testing template
        self.assertTemplateUsed(response, "forms_and_views_app/person_detail.html")

        # testing template's context
        # print("================")
        # print(response.context)  # type: RequestContext
        # print(dir(response.context))
        # print("================")

        # Tutaj sprawdzmy, czy w kontekście szablonu przekazywany jest właściwy obiekt
        context = response.context
        person = context.get("person")
        self.assertIsInstance(person, Person)
        self.assertEqual(person.name, "Jan")

    # test jednostkowy
    def test_create_person_GET(self):
        response = self.client.get(self.create_person_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "forms_and_views_app/person_form.html")

    # test jednostkowy
    def test_create_person_POST(self):

        # Za pomocą klienta testowego możemy również
        # wysyłać zapytania metodą POST (i każdą inną).
        # Parametr `follow`, mówi, czy klient ma wykonać przekierowanie
        # (jeżeli takie zachodzi) i zwrócić to na co jest przekierowanie,
        # czy zatrzymać sie na żądaniu przekierowania (przydatne kiedy chcemy
        # przetestować samo żądanie przekierowania). Domyślnie
        # parametr `follow` jest ustawiony na True, więc bez jawnego ustawienia
        # go na False, nie przetestujemy samego żądania przekierowania.
        response = self.client.post(
            self.create_person_url,
            {
                "name": "Adam",
                "age": 40,
                "city": "Warsaw",
            },
            follow=False,
        )
        self.assertEqual(response.status_code, 302)
        # wszystkie poznane metody orm możemy wykorzystywać w testach
        self.assertEqual(Person.objects.count(), 2)

    # test jednostkowy
    # negatywne scenariusz również powinny zostać przetestowane
    def test_project_detail_POST_no_data(self):

        response = self.client.post(
            self.create_person_url,
            {},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Person.objects.count(), 1)


# następny -> test_models.py
