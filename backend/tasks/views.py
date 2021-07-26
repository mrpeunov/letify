from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category
from tasks.serializers import CategorySerializer, CategoryDetailSerializer, DetailTaskSerializer
from .services.get_task_detail import get_task_detail


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
        return Category.objects.all()
        # return Category.objects.filter(creator=self.request.user)


class TaskDetail(APIView):
    """Получение полностью задания"""
    def get(self, request, pk):
        task = get_task_detail(pk)
        serializer = DetailTaskSerializer(task)
        return Response(serializer.data)


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

-задача полностью:
    -создать
    -удалить
    -обновить
    
-список всех задач пользователя 
    - фильтрация
    - пагинация

-получить задание с определенным вариантом

-получить правильный ответ по варианту и заданию

-поменять категорию для задачи
"""