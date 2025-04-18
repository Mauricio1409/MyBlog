from rest_framework.serializers import ModelSerializer
from post.models import Post
from User.api.serializers import UserSerializer
from category.api.serializers import CategorySerializer


class PostSerializer(ModelSerializer):
    user = UserSerializer()
    category = CategorySerializer()
    class Meta : 
        model = Post
        fields = ['title', 'content', 'slug', 'miniature', 'created_at', 'published', 'user', 'category']