from django.urls import path
from django.shortcuts import render
from .views import index

app_name = 'dashboard'

urlpatterns = [
    path('', index),
]
