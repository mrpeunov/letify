from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, viewsets
from django.shortcuts import get_object_or_404
from rest_framework import permissions

from .models import Category
from .serializer import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]

    serializers = {
        'detail': CategorySerializer,
        'default': CategorySerializer
    }

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.serializers['detail']
        else:
            return self.serializers['default']

    def get_queryset(self):
        return Category.objects.all()
        # return Category.objects.filter(creator=self.request.user)


# class TaskViewSet(viewsets.ModelViewSet):
#
#     serializers = {
#         'detail': DetailTaskSerializer,
#         'list': SnippetTaskSerializer,
#         'default': CreateUpdateTaskSerializer
#     }
#
#     def get_serializer_class(self):
#         if self.action == 'retrieve':
#             return self.serializers['detail']
#         elif self.action == 'list':
#             return self.serializers['list']
#         else:
#             return self.serializers['default']
#
#     def get_queryset(self):
#         return Task.objects.filter(category__creator=self.request.user)


"""
/task/1/variant/ - выдается рандомный вариант задания
/task/1/variant/1/ - выдается 
"""

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

-получить задание с определенным вариантом

-получить правильный ответ по варианту и заданию

-поменять категорию для задачи
"""