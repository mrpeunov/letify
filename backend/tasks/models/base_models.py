from abc import abstractmethod

from django.db import models
from users.models import CustomUser


class Category(models.Model):
    title = models.CharField("Название категории", max_length=120)
    author = models.ForeignKey(CustomUser, verbose_name="Создатель", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Task(models.Model):
    """
    Класс в котором хранится основные характеристики задания
    Должен использоваться для поиска и управления задачей,
    а не для контента задачи
    Контент реализуется через композицию
    """

    class Type(models.TextChoices):
        TEST = "T", "Test"
        MULTIPLE_TEST = "MT", "Multiple Test"
        DEFAULT = "D", "DEFAULT"

    title = models.CharField("Название", max_length=128)

    category = models.ForeignKey(
        Category, verbose_name="Категория", related_name='tasks', on_delete=models.SET_NULL, null=True
    )

    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_date = models.DateTimeField("Дата обновления", auto_now_add=True)
    type = models.CharField("Тип задачи", max_length=10, choices=Type.choices, default=Type.DEFAULT)

    def __str__(self):
        return 'Задание {}'.format(self.title)

    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"


class TaskContent(models.Model):
    """
    Абстрактный класс, насладедники которого определяют в каком формате хранится задание
    """
    task = models.OneToOneField(Task, on_delete=models.CASCADE)
    text = models.TextField("Текст задачи")

    class Meta:
        abstract = True

    @abstractmethod
    def get_all_variants(self):
        pass

    @abstractmethod
    def get_random_variant(self):
        pass

    @abstractmethod
    def check_answer_correctness(self, variant, answer):
        pass
