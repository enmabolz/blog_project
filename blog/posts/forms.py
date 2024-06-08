from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Post, Comment

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'post_image']  

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  
        
        super(PostCreateForm, self).__init__(*args, **kwargs)
        
        
class CommentCreateForm(forms.Form):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',  
                'placeholder': 'Write your comment here.',
                'rows':'3',
            }
        ),
        
        label=''   
    )