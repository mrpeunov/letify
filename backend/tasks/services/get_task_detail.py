from tasks.models import Task
from tasks.types_config import TaskTypesConfig


def get_task_detail(pk):
    # берем само задание
    task = Task.objects.get(id=pk)

    # из конфига берем нужную модель контента
    content_model = TaskTypesConfig[task.type]["model"]

    # получаем эту модель
    task.content = content_model.objects.get(task=task)

    return task
