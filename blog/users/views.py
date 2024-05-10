from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.generic import TemplateView
from .forms import LoginForm, RegisterUserForm
from django.views.generic.edit import CreateView
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
                # Redirect to a success page.
                return redirect('posts:post-list')  # Replace 'home' with the name of your homepage URL
            else:
                # Return an 'invalid login' error message.
                messages.error(request, 'Invalid username or password.')
    

class RegisterUserView(CreateView):
    model = CustomUser
    template_name = 'users/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('posts:post-list')
    
    