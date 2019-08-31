from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('key/', views.KeyView.as_view()),
    path('register/', views.RegistrationAPI.as_view()),
    path('login/', views.LoginAPI.as_view()),
    path('user/', views.UserAPI.as_view()),
]


