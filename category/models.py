from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
