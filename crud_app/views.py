from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from crud_app.models import Book


class BookDetailView(DetailView):
    model = Book


class BookListView(ListView):
    model = Book


class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'category', 'price']


class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'category', 'price']


class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy("crud_app:book_list_view")  # no bo gdzie indziej?
