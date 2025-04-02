from django.db import models
from User.models import User
from django.db.models import CASCADE
from post.models import Post


# Create your models here.
class Comments(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=CASCADE, null=True)

    def __str__(self):
        return self.content
    
