"""
Здесь располагаетс конфиг, нужный для добавления новых типов заданий
"""
from tasks.models import Task
from tasks.models.default_models import DefaultTask
from tasks.serializers import DefaultTaskContentSerializer

TaskTypesConfig = \
    {
        Task.Type.DEFAULT.value: {
            "model": DefaultTask,
            "serializer": DefaultTaskContentSerializer
        }
    },
