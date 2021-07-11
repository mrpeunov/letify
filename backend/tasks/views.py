from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, viewsets
from django.shortcuts import get_object_or_404

from .models import Task, Variant, Variable, Category
from .serializer import CreateUpdateTaskSerializer, PreviewTaskSerializer, DetailTaskSerializer, CategorySerializer


class TaskViewSet(viewsets.ViewSet):
    """
    For working with task for him creator
    """

    # permission_classes = [permissions.IsAuthenticated, ]

    def list(self, request):
        """
        tasks = Task.objects.filter(creator=request.user)
        serializer = PreviewTaskSerializer(tasks, many=True)
        """
        categories = Category.objects.filter(creator=request.user)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        task, created = get_object_or_404(Task, id=pk, creator=request.user)
        serializer = DetailTaskSerializer(task)
        return Response(serializer.data)

    def create(self, request):
        task = CreateUpdateTaskSerializer(data=request.data)
        if task.is_valid():
            task.save(creator=request.user)
            return Response({"status": 201})
        else:
            return Response({"status": 400})

    def partial_update(self, request, pk=None):
        """
        Обновление самой задачи и вложенных вариантов (кроме удаления)
        """
        task = CreateUpdateTaskSerializer(
            Task.objects.get(id=pk),
            data=request.data
        )

        if task.is_valid(raise_exception=True):
            task.save()

        return Response(status=200)

    def destroy(self, request, pk=None):
        task = get_object_or_404(Task, id=pk)
        task.delete()
        return Response(status=204)


class RemoveVariant(viewsets.ViewSet):
    def destroy(self, request, pk, variant):
        variant = get_object_or_404(
            Variant,
            task=Task.objects.get(id=pk),
            number=variant
        )
        variant.delete()
        return Response(status=204)


class RemoveVariable(viewsets.ViewSet):
    def destroy(self, request, pk, variable):
        variants = Variant.objects.filter(
            task=Task.objects.get(id=pk)
        )
        for variant in variants:
            variable = Variable.objects.get(variant=variant, variable=variable)
            variable.delete()
        return Response(status=204)


"""
+получить список моих заданий
+создать задание
+изменить задание (с добавлением или изменением вариантов)
+удалить задание
-удалить вариант


?получить задание с сгенерированным вариантом
?получить правильный ответ по варианту и заданию
"""
