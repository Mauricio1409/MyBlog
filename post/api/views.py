from rest_framework.viewsets import ModelViewSet
from post.models import Post
from post.api.serializers import PostSerializer
from post.api.permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class PostViews(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Post.objects.filter(published=True)
    serializer_class = PostSerializer
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category__slug']

