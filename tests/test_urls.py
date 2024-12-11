# SimpleTestCase - jeżeli nie potrzebujemy bazy danych
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from forms_and_views_app.views import (
    hello_template,
    HelloClassView,
    person_detail
)


class TestUrls(SimpleTestCase):

    # testing function-based view urls
    def test_functional_template_url_is_resolves(self):
        url = reverse('forms_and_views_app:template-hello')
        # print(resolve(url))  # zawiera informacje o: func, url_name,
        # app_name, namespace, route, args and kwargs
        view = resolve(url).func

        self.assertEqual(view, hello_template)

    # testing class-based view urls
    def test_class_template_url_is_resolves(self):
        url = reverse('forms_and_views_app:template-hello2')
        print(resolve(url))  # zawiera informacje o: func, url_name,
        # app_name, namespace, route, args and kwargs
        view = resolve(url).func.view_class  # zmiana
        self.assertEqual(view, HelloClassView)

    # testing parametrized url
    def test_parametrized_detail_url_is_resolves(self):
        url = reverse('forms_and_views_app:person_detail', args=[1])
        view = resolve(url).func
        self.assertEqual(view, person_detail)


# -> test_views.py