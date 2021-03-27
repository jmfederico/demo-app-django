"""
Define the Django `urlpatterns` list of routes URLs to views.

For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path

from tasks.views import tasks_view

urlpatterns = [
    path("", tasks_view),
    path("admin/", admin.site.urls),
]
