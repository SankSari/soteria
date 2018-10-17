from django.urls import path
from .views import RegisterView, LoginView, logout_view, ProfileView

app_name = 'user'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('<str:username>/', ProfileView.as_view(), name='profile'),
]
