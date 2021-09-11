from django.db import models
from django.contrib.auth.models import AbstractUser


class Group(models.Model):
    title = models.CharField("Название или номер группы", max_length=32)


class CustomUser(AbstractUser):
    group = models.ForeignKey(Group, on_delete=models.PROTECT, blank=True, null=True)
    is_creator = models.BooleanField("Может ли создавать", default=False)

    class Meta:
        unique_together = ('email', )
