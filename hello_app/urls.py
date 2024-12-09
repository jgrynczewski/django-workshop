from django.urls import path

from hello_app import views

urlpatterns = [
    path("", views.hello),
    path("param/<str:name>/", views.hello_name),
    path("template/<str:name>/", views.hello_template),
    path(
        "isitmonday/",
        views.is_it_monday
    ),
]
