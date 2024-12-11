from django.urls import path

from form_app import views

app_name = 'form_app'

urlpatterns = [
    path("1/", views.form1, name="form1"),
    path("2/", views.form2, name="form2"),
    path("task-list/", views.task_list, name="task_list"),

    # C - CRUD
    path("task/create/", views.task_create_view, name="task_create_view"),
    # R - Read (widok listy)
    path("task/list/", views.task_list_view, name="task_list_view"),
    # R - Read (widok szczegółu)
    path("task/<int:pk>/", views.task_detail_view, name="task_detail_view"),
    # U - Update
    path("task/update/<int:pk>/", views.task_update_view, name="task_update_view"),
    # D - Delete
    path("task/delete/<int:pk>/", views.task_delete_view, name="task_delete_view"),

]