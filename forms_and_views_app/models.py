from django.shortcuts import reverse
from django.db import models


class Message(models.Model):
    CHOICES = [
        ("question", "Pytanie"),
        ("other", "Inne")
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField()
    category = models.CharField(max_length=10, choices=CHOICES)
    subject = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Ticket(models.Model):
    title = models.CharField(max_length=100)
    registered = models.DateTimeField()
    message = models.ForeignKey(Message, on_delete=models.CASCADE)


class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} z {self.city} <{self.age}>"

    # kanoniczny adres modelu
    # (potrzebny przy przekierowaniach po operacjach niebezpiecznych)
    def get_absolute_url(self):
        # Można podać względną ścieżkę, ale lepiej
        return reverse('forms_and_views_app:person_detail', args=(self.id,))
