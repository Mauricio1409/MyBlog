from django.contrib import admin
from comments.models import Comments

# Register your models here.
@admin.register(Comments)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'user', 'post', 'created_at']
