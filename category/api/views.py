from rest_framework.viewsets import ModelViewSet
from category.models import Category
from category.api.serializers import CategorySerializer
from category.api.permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

class CategoryView(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Category.objects.all()
    #queryset = Category.objects.filter(published=True)
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['published', 'title']