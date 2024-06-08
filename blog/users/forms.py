from django import forms
from .models import CustomUser


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class":"form-control", "placeholder":"Username"}
        ),
        
        label=''
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class":"form-control", "placeholder": "Write a comment"}
        ),
        
        label=''
    )


class RegisterUserForm(forms.ModelForm):
    profile_image = forms.ImageField(required=False)
    
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
        user = kwargs.pop('user', None) 
        super(RegisterUserForm, self).__init__(*args, **kwargs)
                
        if not user or user.role != 'ADM':
            del self.fields['role']
            
        for field_name, field in self.fields.items():
            if field_name == 'role':
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'
                field.required = True 
        
        self.fields['profile_image'].required = False
            
            
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
        
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None) 
        super(EditUserForm, self).__init__(*args, **kwargs)
        
        if not user or user.role != 'ADM':
            del self.fields['role']
            
        for field_name, field in self.fields.items():
            if field_name == 'role':
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'
        
         
        self.fields['first_name'].widget.attrs['readonly'] = True
        self.fields['last_name'].widget.attrs['readonly'] = True
        self.fields['username'].widget.attrs['readonly'] = True
    
        

    