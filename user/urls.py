from django.urls import path
from .views import RegisterView, LoginView, logoutView

app_name = 'user'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logoutView, name='logout'),
]
