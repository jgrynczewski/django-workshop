from django import forms

from crud_app.models import Book


class BookForm(forms.ModelForm):
    model = Book
