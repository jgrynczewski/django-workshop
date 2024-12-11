from django.test import TestCase
from django.urls import reverse

from forms_and_views_app.models import Person


class TestViews(TestCase):

    def setUp(self):
        """Run before every single test method"""
        self.template_view_url = reverse('forms_and_views_app:template-hello')
        self.person_detail_url = reverse('forms_and_views_app:person_detail', args=[1])
        self.create_person_url = reverse('forms_and_views_app:create_person')

        Person.objects.create(
            name='Jan',
            age='11',
            city='Cracow'
        )  # ale jeżeli wpis potrzebny byłby wyłącznie na potrzebny
        # jednego testu to równie dobrze można jego tworzenie
        # umieścić bezpośrednio w teście

    def test_template_view_GET(self):

        response = self.client.get(self.template_view_url)
        print(response)  # type: HttpResponse
        print(dir(response))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forms_and_views_app/hello.html')

        content = str(response.content)
        self.assertIn('Hello', content)

    def test_person_detail_GET(self):

        response = self.client.get(self.person_detail_url)

        self.assertEqual(response.status_code, 200)

        # testing template
        self.assertTemplateUsed(response, 'forms_and_views_app/person_detail.html')

        # testing template's context
        # print("================")
        # print(response.context)  # type: RequestContext
        # print(dir(response.context))
        # print("================")

        context = response.context
        person = context.get('person')

        self.assertIsInstance(person, Person)
        self.assertEqual(person.name, 'Jan')

    def test_create_person_GET(self):
        response = self.client.get(self.create_person_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forms_and_views_app/person_form.html')

    def test_create_person_POST(self):

        response = self.client.post(
            self.create_person_url,
            {
                'name': 'Adam',
                'age': 40,
                'city': 'Warsaw',
            },
            follow=False
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Person.objects.count(), 2)

    # negative scenario also should be tested
    def test_project_detail_POST_no_data(self):

        response = self.client.post(
            self.create_person_url,
            {},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Person.objects.count(), 1)


# next -> test_models.py