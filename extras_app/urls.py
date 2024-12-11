from django.urls import path

from extras_app import views

app_name = 'extras_app'

urlpatterns = [
    path('cookies/', views.cookies, name="cookies"),

    # Zastosowanie ciasteczek - messages
    # Ręczne messages
    path('home/', views.home_view, name="home"),
    path('form/', views.form_view, name="form"),

    # Wbudowany framework messages
    path('home2/', views.home_view2, name="home2"),
    path('form2/', views.form_view2, name="form2"),

    path('session/', views.session, name="session"),

    # Zastosowanie sesji
    # system logowania w innej aplikacji
    # koszyk

    path('sync/', views.main_sync_view, name='sync_main_view'),
    path('async/', views.main_async_view, name='async_main_view'),
]