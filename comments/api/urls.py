from rest_framework.routers import DefaultRouter
from comments.api.views import CommentsViewSet

router = DefaultRouter()

router.register(prefix='comments', basename='comments', viewset=CommentsViewSet)
