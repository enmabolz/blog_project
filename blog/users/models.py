from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ("ADM", "Administrator"),
        ("AUT", "Author"),
        ("SUB", "Subscriber"),
    ]
    
    username = models.CharField(max_length=150, unique=True)
    role = models.CharField(max_length=3, choices=ROLE_CHOICES, default='SUB')
    created_at = models.DateTimeField(auto_now_add=True)
    profile_image = models.ImageField(upload_to="images/profile_pics", null=True, blank=True)
    
    
    def save(self, *args, **kwargs) -> None:
        if self.is_superuser:
            self.role = 'ADM'
             
        if not self.pk and not self.username: 
            self.username = self.get_custom_username()
            
        super().save(*args, **kwargs)
    
    
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

    
    