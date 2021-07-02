from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from .views import TaskViewSet

urlpatterns = format_suffix_patterns([
    path("task/", TaskViewSet.as_view(
        {'get': 'list',
         'post': 'create'}
    )),

    path("task/<int:pk>/", TaskViewSet.as_view(
        {'get': 'retrieve',
         'delete': 'destroy',
         'put': 'update'}
    )),
])
