from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):
    ROLES_CHOICES = {
        "ADM": "Administrator",
        "AUT": "Author",
        "SUB": "Subscriber",
    }
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=3, choices=ROLES_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    profile_image = models.ImageField(upload_to="profile_pics")

    def __str__(self):
        return self.user.username
    
    