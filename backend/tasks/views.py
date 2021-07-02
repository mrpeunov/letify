from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, viewsets
from django.shortcuts import get_object_or_404

from .models import Task
from .serializer import CreateTaskSerializer, PreviewTaskSerializer, DetailTaskSerializer


class TaskViewSet(viewsets.ViewSet):
    """
    For working with task for him creator
    """
    permission_classes = [permissions.IsAuthenticated, ]

    def list(self, request):
        tasks = Task.objects.filter(creator=request.user)
        serializer = PreviewTaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        task = get_object_or_404(Task, id=pk, creator=request.user)
        serializer = DetailTaskSerializer(task)
        return Response(serializer.data)

    def create(self, request):
        task = CreateTaskSerializer(data=request.data)
        if task.is_valid():
            task.save(creator=request.user)
            return Response({"status": 201})
        else:
            return Response({"status": 400})


    def destroy(self, request, pk=None):
        task = get_object_or_404(Task, id=pk)
        task.delete()
        return Response(status=204)

"""
+получить список моих заданий
+создать задание
-изменить задание
+удалить задание
-добавить вариант в задания
-изменить вариант задания
-получить задание с сгенерированным вариантом
-получить правильный ответ по варианту и заданию
"""