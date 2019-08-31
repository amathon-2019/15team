from django.urls import path
from . import views

urlpatterns = [
    path('',  views.CouponView.as_view()),
]
