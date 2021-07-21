from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, viewsets
from django.shortcuts import get_object_or_404
from rest_framework import permissions

from .models import Task, Variant, Variable, Category
from .serializer import (CreateUpdateTaskSerializer,
                         SnippetTaskSerializer,
                         DetailTaskSerializer,
                         CategorySerializer,
                         CategoryDetailSerializer)


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]

    serializers = {
        'detail': CategoryDetailSerializer,
        'default': CategorySerializer
    }

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.serializers['detail']
        else:
            return self.serializers['default']

    def get_queryset(self):
        return Category.objects.filter(creator=self.request.user)


class TaskViewSet(viewsets.ModelViewSet):

    serializers = {
        'detail': DetailTaskSerializer,
        'list': SnippetTaskSerializer,
        'default': CreateUpdateTaskSerializer
    }

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.serializers['detail']
        elif self.action == 'list':
            return self.serializers['list']
        else:
            return self.serializers['default']

    def get_queryset(self):
        return Task.objects.filter(category__creator=self.request.user)




"""
+список категорий
+категория:
    +получить категорию полностью
    +удалить
    +обновить

+задача полностью:
    +создать
    +удалить
    +обновить

-список всех задач пользователя 
    - фильтрация
    - пагинация

-получить задание с определнным вариантом

-получить правильный ответ по варианту и заданию

-поменять категорию для задачи
"""