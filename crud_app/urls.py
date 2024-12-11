from django.urls import path

from crud_app import views

app_name = 'crud_app'

urlpatterns = [
    path('create/', views.BookCreateView.as_view(), name='book_create_view'),
    path('list/', views.BookListView.as_view(), name='book_list_view'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='book_detail_view'),
    path('update/<int:pk>/', views.BookUpdateView.as_view(), name='book_update_view'),
    path('delete/<int:pk>/', views.BookDeleteView.as_view(), name='book_delete_view')
]
