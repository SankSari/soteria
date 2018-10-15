from django.urls import path
from django.shortcuts import render
from .views import IndexView

app_name = 'dashboard'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
