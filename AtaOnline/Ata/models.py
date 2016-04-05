"""Models for Ata."""

from django.db import models

# Create your models here.


class User(models.Model):
    """User's docstring."""

    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    number_id = models.IntegerField()
    email = models.EmailField(max_length=200)
    name = models.CharField()
    admin = models.BooleanField()
