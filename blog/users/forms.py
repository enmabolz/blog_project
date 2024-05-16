from django import forms
from .models import CustomUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, ButtonHolder, HTML
from django.contrib.auth.forms import UserCreationForm


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
    
    
    
class RegisterUserForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )

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
                Column('password1', css_class='custom-margin'),
                Column('password2', css_class='custom-margin'),
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
        fields = ['first_name', 'last_name', 'email', 'role', 'profile_image']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        
        return password2


    def clean(self):
        cleaned_data = super().clean()
        required_fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

        for field_name in required_fields:
            if not cleaned_data.get(field_name):
                self.add_error(field_name, "This field is required")

    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        
        if commit:
            user.save()
            
        return user
        
        
class EditUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    role = forms.CharField(max_length=50)
    repeat_password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
        
    def __init__(self, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)
        
        self.fields['first_name'].widget.attrs['readonly'] = True
        self.fields['last_name'].widget.attrs['readonly'] = True
        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['role'].widget.attrs['readonly'] = True
        
    
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
    
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='custom-margin'),
                Column('last_name', css_class='custom-margin'),
                
            ),
            Row(
                Column('username', css_class='custom-margin'),
                Column('email', css_class='custom-margin'),
                
                
            ),
            Row(
                Column('role', css_class='custom-margin'),
                Column('profile_image', css_class='custom-margin'),
            ),
            ButtonHolder(
                Submit('submit', 'Edit User', css_class='btn btn-outline'),
                HTML('<a href="{% url "users:change-password" %}" class="btn btn-outline">Change Password</a>'),
                css_class='d-flex justify-content-between mt-3',
            ),
        )
        
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'username', 'role', 'profile_image']