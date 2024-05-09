from django import forms
from .models import CustomUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, ButtonHolder


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "style": {"margin: 1% 0%"}, "placeholder":"Username"}
        ),
        
        label=''
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "style": {"margin: 1% 0%"}, "placeholder":"Password"}
        ),
        
        label=''
    )
    
    

class RegisterUserForm(forms.ModelForm):
    repeat_password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
    
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='custom-margin'),
                Column('last_name', css_class='custom-margin'),
                Column('email', css_class='custom-margin'),
            ),
            Row(
               
                Column('password', css_class='custom-margin'),
                Column('repeat_password', css_class='custom-margin'),
            ),
            Row(
                Column('role', css_class='custom-margin'),
                Column('profile_image', css_class='custom-margin'),
            ),
            ButtonHolder(
                Submit('submit', 'Register User', css_class='btn btn-outline'),
                css_class='d-grid gap-2',
            )
        )
    
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password', 'repeat_password', 'role', 'profile_image']

    
        
        