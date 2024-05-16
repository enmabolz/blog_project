from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import TemplateView
from .forms import LoginForm, RegisterUserForm, EditUserForm
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from .models import CustomUser
from django.urls import reverse_lazy


class UserLogin(TemplateView):
    def get(self, request):
        form = LoginForm()
        
        return render(request, 'users/login.html', {'form': form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                
                return redirect('posts:post-list')  
            else:
                messages.error(request, 'Invalid username or password.')
    

class RegisterUserView(CreateView):
    model = CustomUser
    template_name = 'users/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('posts:post-list')
    

class EditUser(LoginRequiredMixin, UpdateView):
    form_class = EditUserForm
    model = CustomUser
    template_name = 'users/edit_user.html'
    success_url = reverse_lazy('posts:post-list')
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        instance = self.get_object()
        
        context['first_name'] = instance.first_name
        context['email'] = instance.last_name
        context['profile_image'] = instance.profile_image
        
        return context


class PasswordChangeView(PasswordChangeView):
    template_name = 'users/password_change.html'
    
    
class PasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'users/password_change_done.html'