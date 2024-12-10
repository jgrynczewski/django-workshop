from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=64)
    capital = models.OneToOneField('Capital', on_delete=models.CASCADE)


class Capital(models.Model):
    name = models.CharField(max_length=64)


class Language(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"


class Framework(models.Model):
    name = models.CharField(max_length=64)
    language = models.ForeignKey('Language', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.language})"


class Actor(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"


class Movie(models.Model):
    title = models.CharField(max_length=128)
    actors = models.ManyToManyField('Actor')

    def __str__(self):
        return f"{self.title}"
