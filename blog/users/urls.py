from django.urls import path
from .views import UserLogin, RegisterUserView

app_name = 'users'

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
]
