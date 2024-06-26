from django.urls import path
from .views import PostList, PostDetails, PostCreation, PostDelete, PostUpdate

app_name = 'posts'

urlpatterns = [
    path('', PostList.as_view(), name='post-list'),
    path('create', PostCreation.as_view(), name='post-create'),
    path('<int:pk>/details', PostDetails.as_view(), name='post-details'),
    path('<int:pk>/delete', PostDelete.as_view(), name='post-delete'),
    path('<int:pk>/update', PostUpdate.as_view(), name='post-update'),
] 

