from django.urls import path
from .views import SearchView

app_name = 'disaster'

urlpatterns = [
    path('q/', SearchView.as_view(), name='search'),
]
