from rest_framework.serializers import ModelSerializer
from category.models import Category

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'slug', 'published']