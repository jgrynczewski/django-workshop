# FORMULARZE DJANGO i FORMULARZE MODELU
from django.shortcuts import (
    render, redirect, HttpResponse,
    get_object_or_404,
)
from django.views import View
from django.views.generic import TemplateView, DetailView, CreateView

from forms_and_views_app.models import Message, Person
from forms_and_views_app.forms import MessageForm, MessageModelForm, PersonForm



#### FORMULARZE

# HTML form - dotychczasowy sposób pracy z formularzami
def contact1(request):
    if request.method == "GET":
        return render(request, 'forms_and_views_app/form1.html')

    else:
        data = request.POST

        # do zrobienia walidacja danych formularza

        Message.objects.create(
            name=data.get('name'),
            email=data.get('email'),
            category=data.get('category'),
            subject=data.get('subject'),
            body=data.get('body'),
            date=data.get('date'),
            time=data.get('time')
        )

        return redirect("forms_and_views_app:contact1")


# Django form
def contact2(request):
    if request.method == "GET":
        form = MessageForm()  # unbound form
        # print(form)
        return render(
            request,
            'forms_and_views_app/form2.html',
            {'form': form}
        )

    else:
        form = MessageForm(request.POST)  # bound form

        if form.is_valid():
            data = form.cleaned_data
            Message.objects.create(
                name=data.get('name'),
                email=data.get('email'),
                category=data.get('category'),
                subject=data.get('subject'),
                body=data.get('body'),
                date=data.get('date'),
                time=data.get('time')
            )
            return redirect("forms_and_views_app:contact2")

    return render(
        request,
        'forms_and_views_app/form2.html',
        {"form": form}
    )


# Django Model Form (formularz modelu)
def contact3(request):
    if request.method == "GET":
        form = MessageModelForm()  # unbound form

        return render(
            request,
            'forms_and_views_app/form3.html',
            {"form": form}
        )

    if request.method == "POST":
        form = MessageModelForm(request.POST)  # bound form
        if form.is_valid():
            form.save()
            return redirect("forms_and_views_app:contact3")

        return render(
            request,
            'forms_and_views_app/form3.html',
            {"form": form}
        )


#### WIDOKI

# function-based view
def hello(request):
    return HttpResponse("Hello, world!")


# class-based view
class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello, world!")


# A jak z szablonami ?
# Widok funkcyjny
def hello_template(request):
    return render(
        request,
        'forms_and_views_app/hello.html',
    )

# Widok klasowy
class HelloClassView(View):
    def get(self, request):
        return render(
            request,
            'forms_and_views_app/hello.html'
        )

# Widok generyczny
class HelloGenericView(TemplateView):
    template_name = 'forms_and_views_app/hello.html'
# A można jeszcze krócej - patrz urlpatterns 'hello4/'


# A co jeżeli chcemy przekazać do szablonu jakąś zmienną?
# Widok funkcyjny
def hello_template2(request):
    name = "Jan"

    return render(
        request,
        'forms_and_views_app/hello2.html',
        context = {
            'name': name
        }
    )

# Widok klasowy
class HelloClassView2(View):
    def get(self, request):
        name = "Jan"

        return render(
            request,
            'forms_and_views_app/hello2.html',
            context={
                'name': name
            }
        )

# Widok generyczny
class HelloGenericView2(TemplateView):
    template_name = 'forms_and_views_app/hello2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = "Jan"
        return context


# A jak z modelami ?
# Widok detalu - R (CRUD)
# Zróbmy widok, który wyświetli nam szczegóły wskazanego wpisu z tabelki.

# function-based view
def person_detail(request, id):
    p = get_object_or_404(Person, id=id)
    return render(request, 'forms_and_views_app/person_detail.html', {"person": p})


# class-based view
class PersonView(View):
    def get(self, request, id):
        p = get_object_or_404(Person, id=id)
        return render(request, 'forms_and_views_app/person_detail.html', {"person": p})


# generic view
# https://docs.djangoproject.com/en/5.1/ref/class-based-views/generic-display/#detailview
class PersonDetailView(DetailView):
    model = Person
    # DetailView szuka szablonu o nazwie person_detail.html

# Popatrzmy jeszcze na inny widok (tym razem z formularzem)
# C(CRUD)

# function-based view
def create_person(request):
    if request.method == "GET":
        form = PersonForm()
        return render(
            request,
            'forms_and_views_app/person_form.html',
            {"form": form}
        )
    else:
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save()
            return redirect(person.get_absolute_url())

        else:
            return render(
                request,
                'forms_and_views_app/person_form.html',
                {"form": form}
            )


# Class-based view
class PersonCreateView(View):
    def get(self, request):
        form = PersonForm()
        return render(
            request,
            'forms_and_views_app/person_form.html',
            {"form": form}
        )

    def post(self, request):
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save()
            return redirect(person.get_absolute_url())

        else:
            return render(
                request,
                'forms_and_views_app/person_form.html',
                {"form": form}
            )


# Generic view
class PersonCreateView2(CreateView):
    # CreateView szuka szablonu person_form.html
    model = Person
    fields = '__all__'
    # do przekierowania wykorzystuje get_absolute_url
    # można też użyć atrybutu klasowego `success_url`

# I dużo więcej
# https://docs.djangoproject.com/en/5.1/ref/class-based-views/
