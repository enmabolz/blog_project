from django.urls import path
from .views import UserLogin, RegisterUserView, EditUser, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.views import LogoutView


app_name = 'users'

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('<int:pk>/edit', EditUser.as_view(), name='edit'),
    path('password_change/', PasswordChangeView.as_view(), name='change-password'),
    path('password_change_done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
]
