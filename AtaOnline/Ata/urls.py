"""Ata urls."""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', (views.index)),
    url(r'^/ata/', views.index, name="index"),
]