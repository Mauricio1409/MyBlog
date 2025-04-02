from rest_framework.viewsets import ModelViewSet
from comments.models import Comments
from comments.api.serializers import CommentsSrializer
from django_filters.rest_framework import OrderingFilter, DjangoFilterBackend
from comments.api.permmisions import IsOwnerOrReadAndCreateOnly


class CommentsViewSet(ModelViewSet):
    permission_classes = [IsOwnerOrReadAndCreateOnly]
    queryset = Comments.objects.all()
    serializer_class = CommentsSrializer
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['post']
    OrderingFilter = ['created_at']