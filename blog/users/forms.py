from django import forms
from .models import CustomUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, ButtonHolder, HTML
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder":"Username"}
        ),
        
        label=''
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder":"Password"}
        ),
        
        label=''
    )


class RegisterUserForm(forms.ModelForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput,
        label='Password'
    )
    
    password2 = forms.CharField(
        widget=forms.PasswordInput,
        label='Confirm Password'
    )
    
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'role', 'profile_image']
        
        
        
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            if field_name == 'role':
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'
                field.required = True 
            
    def clean(self):
        cleaned_data = super().clean()
        
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Passwords do not match")

        return cleaned_data


    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        
        if commit:
            user.save()
        
        return user
    
    
        
class EditUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'username', 'role', 'profile_image']
        
    username = forms.CharField(max_length=100)
    role = forms.CharField(max_length=50)
        
        