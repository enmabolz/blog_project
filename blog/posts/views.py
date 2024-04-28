from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post


class PostList(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'post_list'
    
        
class PostDetails(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
    
    
class PostCreation(CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = ['title', 'content']
    
    
class PostUpdate(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title', 'content', 'created_at', 'likes', 'dislikes']
    
    
class PostDelete(DeleteView):
    pass

