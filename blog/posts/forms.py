from django import forms
from .models import Post

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'post_image']  

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  
        
        super(PostCreateForm, self).__init__(*args, **kwargs)