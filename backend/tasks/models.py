from django.db import models

from users.models import CustomUser


class Task(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name="Создатель", on_delete=models.CASCADE)
    title = models.CharField("Название", max_length=128)
    content = models.TextField("Задача")
    withAnswer = models.BooleanField("Есть ответ", default=False)


class Option(models.Model):
    json = models.JSONField()
