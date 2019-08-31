from django.urls import path
from . import views

urlpatterns = [
    path('key/', views.KeyView.as_view()),
    path('auth/register', views.RegistrationAPI.as_view()),
    path('auth/login', views.LoginAPI.as_view()),
    path('auth/user', views.UserAPI.as_view())
]
