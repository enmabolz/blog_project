from django.db import models
from users.models import CustomUser

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    partial_content_to_show = models.CharField(max_length=300, blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    post_image = models.ImageField(upload_to="images/post_images", null=True, blank=True)
    
    def save(self, *args, **kwargs):
        self.partial_content_to_show = self.content[0:300]
        
        super().save(*args, **kwargs)
        
    
    def __str__(self):
        return f"{self.title}.{self.author}"