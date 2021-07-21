from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from .views import (TaskViewSet,
                    CategoryViewSet)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'task', TaskViewSet, basename='task')
urlpatterns = router.urls


