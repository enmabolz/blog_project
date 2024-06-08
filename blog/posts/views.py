from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import PostCreateForm, CommentCreateForm


class PostList(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'post_list'
            
            
class PostDetails(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object)
        context['comment_form'] = CommentCreateForm
        
        return context

        
    def post(self, request, *args, **kwargs):
        post_id = request.POST.get('post_id')
        action = request.POST.get('action')
        
        if post_id and action:
            post = Post.objects.get(pk=post_id)
            
            if action == 'like':
                post.likes += 1
            elif action == 'dislike':
                post.dislikes += 1
            elif action == 'comment':
                comment_form = CommentCreateForm(request.POST)
                if comment_form.is_valid():
                    content = comment_form.cleaned_data['content']
                    Comment.objects.create(user=request.user, post=post, content=content)
            
            post.save()
            
            return HttpResponseRedirect(request.path + '#end')
        
        
        return super().post(request, *args, **kwargs)
            
            
class PostCreation(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    template_name = 'posts/post_create.html'
    form_class = PostCreateForm
    success_url = reverse_lazy('posts:post-list')
    
    def test_func(self):
        return self.request.user.role == 'ADM' or self.request.user.role == 'AUT'
    
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        
        kwargs['user'] = self.request.user  

        return kwargs
    
    
class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'posts/post_confirm_delete.html'
    success_url = reverse_lazy('posts:post-list')
    context_object_name = 'post'
    
    def test_func(self):
        return self.request.user.role == 'ADM' or self.request.user.id == self.kwargs['pk']
    
    
class PostUpdate(UpdateView):
    model = Post
    template_name = 'posts/post_update.html'
    fields = ['title', 'post_image', 'content']
    success_url = reverse_lazy('posts:post-list')
               
            
        
        
    
    