from django.urls import path
from . import views

urlpatterns = [
    path('',  views.myAPI.as_view()),
]
