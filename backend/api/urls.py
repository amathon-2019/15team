from django.urls import path
from . import views

urlpatterns = [
    path('key/',views.KeyView.as_view()),
    path('main/<str:key>', views.MainView.as_view())
]
