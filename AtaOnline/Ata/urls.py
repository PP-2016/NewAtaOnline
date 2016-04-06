"""Ata urls."""

from django.conf.urls import url
from .views import Login, Index
urlpatterns = [
    url(r'^$', Index.as_view(), name="index"),
    url(r'^login/$', Login.as_view(), name="login"),
]
