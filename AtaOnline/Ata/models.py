"""Models for Ata."""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Student(User, models.Model):
    """Student's docstring."""

    number_id = models.IntegerField()


class Professor(User, models.Model):
    """Professor's docstring."""

    number_id = models.IntegerField()
    formation = models.CharField(max_length=200)


class Avaliation(models.Model):
    """Avaliation from a Professor for a Student's Notebook."""

    record = models.ForeignKey('Notebook')


class Notebook(models.Model):
    """Student's Notebook for class of Experimental Fisics."""

    title = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    content = models.CharField(max_length=250)
    grade = models.ForeignKey('Avaliation')
