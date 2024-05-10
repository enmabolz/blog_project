from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


class PostList(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'post_list'
            
            
class PostDetails(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'
    
    def post(self, request, *args, **kwargs):
        post_id = request.POST.get('post_id')
        action = request.POST.get('action')
        
        if post_id and action:
            post = Post.objects.get(pk=post_id)
            
            if action == 'like':
                post.likes += 1
            elif action == 'dislike':
                post.dislikes += 1
            
            post.save()
            return HttpResponseRedirect(request.path + '#end')
        
        return super().post(request, *args, **kwargs)
            
class PostCreation(CreateView):
    model = Post
    template_name = 'posts/post_create.html'
    fields = ['title', 'post_image', 'content']
    success_url = reverse_lazy('posts:post-list')    
    
    
class PostDelete(DeleteView):
    model = Post
    template_name = 'posts/post_confirm_delete.html'
    success_url = reverse_lazy('posts:post-list')
    context_object_name = 'post'
    
    
class PostUpdate(UpdateView):
    model = Post
    template_name = 'posts/post_update.html'
    fields = ['title', 'post_image', 'content']
    success_url = reverse_lazy('posts:post-list')