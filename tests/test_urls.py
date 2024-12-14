# SimpleTestCase - jeżeli nie potrzebujemy bazy danych
# (wtedy django nie tworzy testowej bazy danych)
from django.test import SimpleTestCase
from django.urls import reverse, resolve

# przetestujmy kilka rzeczy z aplikacji forms_and_views_app
from forms_and_views_app.views import hello_template, HelloClassView, person_detail


class TestUrls(SimpleTestCase):

    # testing function-based view urls
    def test_functional_template_url_is_resolves(self):
        url = reverse("forms_and_views_app:template-hello")
        # print(resolve(url))  # zawiera informacje o: func, url_name,
        # app_name, namespace, route, args and kwargs
        view = resolve(url).func

        # asercjami możemy sobie porównać czy wszystko z obiektu
        # zwracanego przez funkcję `resolve` się zgadza, na przykład
        # widok:
        self.assertEqual(view, hello_template)
        # Ale klasa zawiera zbiór asercji dedykowanych do testowania
        # aplikacji webowych. Na przykład assertTemplateUsed - co zobaczymy
        # kolejnej suicie (test_views.py)

    # testing class-based view urls
    def test_class_template_url_is_resolves(self):
        url = reverse("forms_and_views_app:template-hello2")
        print(resolve(url))  # to samo co w poprzednim
        view = resolve(url).func.view_class  # uwaga, tutaj
        # trochę inaczej niż w widoku funkcyjnym
        self.assertEqual(view, HelloClassView)

    # a jak to samo będzie wyglądało przy sparametryzowanym endpoincie?
    def test_parametrized_detail_url_is_resolves(self):
        url = reverse("forms_and_views_app:person_detail", args=[1])
        view = resolve(url).func
        self.assertEqual(view, person_detail)


# następny -> test_views.py
