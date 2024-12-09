from django.urls import path

from hello_app import views

app_name = 'hello_app'

urlpatterns = [
    path("", views.hello),
    path("param/<str:name>/", views.hello_name),
    path("template/<str:name>/", views.hello_template),
    path(
        "isitmonday/",
        views.is_it_monday
    ),
    path("dtl/", views.dtl),

    path("first/", views.first_view, name="first"),
    path("second/", views.second_view, name="second"),
    path("third/<str:param>/", views.third_view, name="third"),

    path("child1/", views.child1_view, name="child1"),
    path("child2/", views.child2_view, name="child2"),
]
