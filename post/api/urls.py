from rest_framework.routers import DefaultRouter
from post.api.views import PostViews

router = DefaultRouter()

router.register(prefix='post', basename='post', viewset=PostViews)