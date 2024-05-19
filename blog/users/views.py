from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.views.generic import TemplateView
from .forms import LoginForm, RegisterUserForm, EditUserForm
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from .models import CustomUser
from django.urls import reverse_lazy, reverse


class UserList(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = CustomUser
    template_name = 'users/user_list.html'
    context_object_name = 'user_list'
    
    def test_func(self):
        return self.request.user.role == 'ADM'
        
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
                return render(request, 'users/login.html', {'form': form, 'messages': messages.get_messages(request)})
            
        return render(request, 'users/login.html', {'form': form, 'messages': messages.get_messages(request)})


class RegisterUserView(CreateView):
    model = CustomUser
    template_name = 'users/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('posts:post-list')
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        
        if self.request.user.is_authenticated: 
            kwargs['user'] = self.request.user
            
        return kwargs
    
    
    def form_valid(self, form):
        new_user = form.save()
        
        if not self.request.user.is_authenticated:
            user = authenticate(
                username=new_user.username,
                password=form.cleaned_data['password1']
            )
            
            if user is not None:
                login(self.request, user)
                messages.success(
                    self.request, f'User created successfully. You are logged in as: {user.username}.'
                    )
                
                return redirect(reverse('posts:post-list')) 
        else:
            messages.success(
                    self.request, f'User with username "{new_user.username}" created successfully.'
                )
            
        return super().form_valid(form)
    

class EditUser(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    form_class = EditUserForm
    model = CustomUser
    template_name = 'users/edit_user.html'
    success_url = reverse_lazy('posts:post-list')
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        instance = self.get_object()
        
        context['first_name'] = instance.first_name
        context['email'] = instance.email
        context['profile_image'] = instance.profile_image
        
        return context
    
    
    def test_func(self):
        return self.request.user.role == 'ADM' or self.kwargs['pk'] == self.request.user.id
    
    
    def form_valid(self, form):
        form.save()
        
        messages.success(
                    self.request, 'User edited successfully!!'
                )
        
        return super().form_valid(form)
        

class PasswordChange(LoginRequiredMixin, UserPassesTestMixin, PasswordChangeView):
    template_name = 'users/password_change.html'
    success_url = reverse_lazy('posts:post-list')
    
    def test_func(self):
        return self.request.user.role == 'ADM' or self.kwargs['pk'] == self.request.user.id
    
    
