from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLES_CHOICES = {
        "ADM": "Administrator",
        "AUT": "Author",
        "SUB": "Subscriber",
    } 
    
    username = models.TextField(unique=True)
    role = models.CharField(max_length=3, choices=ROLES_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    profile_image = models.ImageField(upload_to="profile_pics", blank=True)
    
    def save(self, *args, **kwargs) -> None:
        self.username = self.get_custom_username()
        return super().save(*args, **kwargs)
    
    def get_custom_username(self):
        base_username = f"{self.first_name.lower()}.{self.last_name.lower()}"
        username = base_username
        counter = 1
    
        while CustomUser.objects.filter(username=username).exists():
            username = f"{base_username}{counter}"
            counter += 1
    
        return username
            
    
    def __str__(self):
        return self.username
    
    