from django.db import models
from tasks.models.base import AbstractTask
from users.models import CustomUser


class Competition(models.Model):
    title = models.CharField("Название соревнования", max_length=128)
    creator = models.ForeignKey(CustomUser, verbose_name="Создатель", on_delete=models.SET_NULL, null=True)
    start = models.DateTimeField("Начало", null=True)
    finish = models.DateTimeField("Конец", null=True)
    tasks = models.ManyToManyField(AbstractTask)

    class Meta:
        verbose_name = "Соревнование"
        verbose_name_plural = "Соревнования"


class Attempt(models.Model):
    """Попытка прохождения соревнования"""
    user = models.ForeignKey(CustomUser, verbose_name="Пользователь", on_delete=models.SET_NULL, null=True)
    competition = models.ForeignKey(Competition, verbose_name="Соревнование", on_delete=models.SET_NULL, null=True)
    result = models.IntegerField("Результат")
    max_result = models.IntegerField("Максимальный результат")

    class Meta:
        verbose_name = "Попытка"
        verbose_name_plural = "Попытки"


class TaskAnswer(models.Model):
    """Ответ на одно задание"""
    attempt = models.ForeignKey(Attempt, on_delete=models.CASCADE)
    user_answer = models.CharField("Ответ пользователя", max_length=128)
    correct_answer = models.CharField("Правильный ответ", max_length=128)
    grade = models.IntegerField("Оценка")
    max_grade = models.IntegerField("Максимальная оценка")

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
