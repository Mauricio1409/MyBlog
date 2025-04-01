from rest_framework.routers import DefaultRouter
from category.api.views import CategoryView

router = DefaultRouter()

router.register(prefix="category", viewset=CategoryView, basename="category")