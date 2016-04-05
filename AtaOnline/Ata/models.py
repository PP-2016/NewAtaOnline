"""Models for Ata."""

from django.db import models

# Create your models here.


class Person(models.Model):
    """Models for AtaOnline's user."""

    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    number_id = models.IntegerField()
    email = models.EmailField(max_length=200)
    name = models.CharField(max_length=50)
    admin = models.BooleanField()


class Student(models.Person, models.Model):
    """Student's docstring."""


class Professor(models.Person, models.Model):
    """Professor's docstring."""

    formation = models.CharField(max_length=200)


# class Avaliation(models.Model):
#     """Avaliation from a Professor for a Student's Notebook."""
#     ata = Fo

class Notebook(models.Model):
    """Student's Notebook for class of Experimental Fisics."""

    title = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    content = models.CharField(max_length=150)
    avaliation = models.OneToOneField()
