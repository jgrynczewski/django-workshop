from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from api import views

app_name = 'api'

# https://www.django-rest-framework.org/
urlpatterns = [
    path ('v1/message/', views.message_list, name='message_list'),
    path ('v2/message/', views.MessageView.as_view(), name='message_list2'),
    path ('v3/message/', views.MessageListCreateView.as_view(), name='message_list3'),

    # swagger
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "schema/docs/",
        SpectacularSwaggerView.as_view(url_name="api:schema"),
        name="swagger-docs",
    ),
]

# Autmoatyczny klient na bazie schematu openAPI
# https://github.com/OpenAPITools/openapi-generator
# https://github.com/openapi-generators/openapi-python-client
