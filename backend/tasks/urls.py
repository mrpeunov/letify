from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from .views import TaskViewSet, RemoveVariant, RemoveVariable, CategoryViewSet, TestView

urlpatterns = format_suffix_patterns([
    path("task/", TaskViewSet.as_view(
        {'get': 'list',
         'post': 'create'}
    )),

    path("test/", TestView.as_view()),

    path("task/<int:pk>/", TaskViewSet.as_view(
        {'get': 'retrieve',
         'delete': 'destroy',
         'patch': 'partial_update'}
    )),

    path("task/<int:pk>/variant/<int:variant>/", RemoveVariant.as_view(
        {'delete': 'destroy'}
    )),

    path("task/<int:pk>/variable/<str:variable>/", RemoveVariable.as_view(
        {'delete': 'destroy'}
    )),

    path("category/", CategoryViewSet.as_view(
        {'post': 'create'}
    )),

    path("category/<int:pk>/", CategoryViewSet.as_view(
        {'patch': 'partial_update'}
    ))
])
