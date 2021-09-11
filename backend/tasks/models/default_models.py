from django.db import models
from tasks.models.base_models import TaskContent


class DefaultTask(TaskContent):

    def get_all_variants(self):
        pass

    def get_random_variant(self):
        pass

    def check_answer_correctness(self, answer):
        pass


class DefaultTaskVariant(models.Model):
    """Вариант задания"""
    task = models.ForeignKey(DefaultTask, related_name='variants', verbose_name="Задание", on_delete=models.CASCADE)
    number = models.IntegerField("Номер варианта")
    answer = models.CharField("Ответ", max_length=128)

    class Meta:
        db_table = "default_task_variant"
        verbose_name = "Вариант задания"
        verbose_name_plural = "Варианты задания"


class VariableForDefaultTask(models.Model):
    """Переменная для обычных тасков"""
    variant = models.ForeignKey(
        DefaultTaskVariant, related_name='variables', verbose_name="Вариант", on_delete=models.CASCADE
    )
    name = models.CharField("Название переменной", max_length=32)
    value = models.CharField("Значение", max_length=256)

    class Meta:
        db_table = "variable_for_default_task"
        verbose_name = "Переменная для варианта"
        verbose_name_plural = "Переменные для варианта"



