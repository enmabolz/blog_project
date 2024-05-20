from django.urls import path
from .views import UserList, UserLogin, RegisterUserView, EditUser, PasswordChange, UserDetail
from django.contrib.auth.views import LogoutView


app_name = 'users'

urlpatterns = [
    path('list/', UserList.as_view(), name='user-list'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('<int:pk>/edit', EditUser.as_view(), name='edit'),
    path('<int:pk>/password_change/', PasswordChange.as_view(), name='change-password'),
    path('<int:pk>/details', UserDetail.as_view(), name='user-details')
]
