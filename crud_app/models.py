from django.db import models
from django.urls import reverse

CATEGORIES = [
    (1, "Comedy"),
    (2, "Thriller"),
    (3, "Romance"),
]


class Book(models.Model):
    added = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=256)
    category = models.IntegerField(choices=CATEGORIES)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('crud_app:book_list_view')
