"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

urlpatterns = [
    path('manage/', include('backend.manage.urls')),
    path('api-<str:key>/', include('backend.api.urls')),
    path('api/admin/', admin.site.urls),
]


