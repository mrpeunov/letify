from rest_framework import serializers
from tasks.models import Category, Task
from .default_task_serializers import DefaultTaskContentSerializer


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'created_date', 'updated_date', 'type')


class DetailTaskSerializer(serializers.ModelSerializer):
    content = DefaultTaskContentSerializer(many=False)

    class Meta:
        model = Task
        fields = ('id', 'title', 'created_date', 'updated_date', 'type', 'content')


class CategoryDetailSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True)

    class Meta:
        model = Category
        fields = ('id', 'title', 'tasks')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')
