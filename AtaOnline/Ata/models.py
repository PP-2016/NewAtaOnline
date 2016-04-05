"""Models for Ata."""

from django.db import models

# Create your models here.


class AbstractPerson(models.Model):
    """Models for AtaOnline's user."""

    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    number_id = models.IntegerField()
    email = models.EmailField(max_length=200)
    name = models.CharField(max_length=50)
    admin = models.BooleanField()

    class Meta:
        """Abstract class needs a Meta."""

        abstract = True


class Student(AbstractPerson, models.Model):
    """Student's docstring."""


class Professor(AbstractPerson, models.Model):
    """Professor's docstring."""

    formation = models.CharField(max_length=200)


class Avaliation(models.Model):
    """Avaliation from a Professor for a Student's Notebook."""

    record = models.ForeignKey('Notebook')


class Notebook(models.Model):
    """Student's Notebook for class of Experimental Fisics."""

    title = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    content = models.CharField(max_length=150)
    grade = models.ForeignKey('Avaliation')
