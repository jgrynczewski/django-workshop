from django.urls import path
from django.views.generic import TemplateView

from forms_and_views_app import views

app_name = "forms_and_views_app"

urlpatterns = [
    # forms
    path("contact1/", views.contact1, name="contact1"),
    path("contact2/", views.contact2, name="contact2"),
    path("contact3/", views.contact3, name="contact3"),

    # views
    path('hello/', views.hello, name='hello'),
    path('hello2/', views.HelloView.as_view(), name='hello2'),

    path('template/hello/', views.hello_template, name='template-hello'),
    path('template/hello2/', views.HelloClassView.as_view(), name='template-hello2'),
    path('template/hello3/', views.HelloGenericView.as_view(), name='template-hello3'),
    path(
        'template/hello4/',
        TemplateView.as_view(template_name="forms_and_views_app/hello.html"),
        name='template-hello4'
    ),

    path('template2/hello/', views.hello_template2, name='template2-hello'),
    path('template2/hello2/', views.HelloClassView2.as_view(), name='template2-hello2'),
    path('template2/hello3/', views.HelloGenericView2.as_view(), name='template2-hello3'),

    path('person/<int:id>/', views.person_detail, name='person_detail'),
    path('person2/<int:id>/', views.PersonView.as_view(), name='person_detail2'),
    # Uwaga! Tutaj musi być pk (ew. slug), a nie id.
    path('person3/<int:pk>/', views.PersonDetailView.as_view(), name='person_detail3'),

    path('create-person/', views.create_person, name='create_person'),
    path('create-person2/', views.PersonCreateView.as_view(), name='person_view'),
    path('create-person3/', views.PersonCreateView2.as_view(), name='create_person_view')

]
