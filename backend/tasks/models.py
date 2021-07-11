from django.db import models
from users.models import CustomUser


class Category(models.Model):
    title = models.CharField("Название категории", max_length=120)
    creator = models.ForeignKey(CustomUser, verbose_name="Создатель", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Task(models.Model):
    """Шаблон задания"""
    creator = models.ForeignKey(CustomUser, verbose_name="Создатель", on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, verbose_name="Категория", related_name='tasks', on_delete=models.SET_NULL, null=True)
    title = models.CharField("Название", max_length=128)
    content = models.TextField("Задача")
    grade = models.IntegerField("Максимальная оценка")
    withAnswer = models.BooleanField("Есть ответ", default=False)
    withSelfChecking = models.BooleanField("Самопроверяемый", default=False)
    option_count = models.IntegerField("Количество вариантов", default=0)

    def __str__(self):
        return 'Задание {}'.format(self.title)

    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"


class Variant(models.Model):
    """Вариант задания"""
    task = models.ForeignKey(Task, related_name='variants', verbose_name="Задание", on_delete=models.CASCADE)
    number = models.IntegerField("Номер варианта")
    answer = models.CharField("Ответ", max_length=128)

    class Meta:
        verbose_name = "Вариант задания"
        verbose_name_plural = "Варианты задания"


class Variable(models.Model):
    """Переменная для варианта"""
    variant = models.ForeignKey(Variant, related_name='variables', verbose_name="Вариант", on_delete=models.CASCADE)
    variable = models.CharField("Переменная", max_length=32)
    value = models.CharField("Значение", max_length=256)

    class Meta:
        verbose_name = "Переменная для варианта"
        verbose_name_plural = "Переменные для варианта"
