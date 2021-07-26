from tasks.models.base_models import TaskContent
from django.db import models


class TestTask(TaskContent):
    answer = models.IntegerField("Номер правильного ответа")

    def get_all_variants(self):
        pass

    def get_random_variant(self):
        pass

    def check_answer_correctness(self, answer):
        pass


class OptionForTestTask(models.Model):
    """
    Варианты задания для теста
    """
    task = models.ForeignKey(TestTask, related_name="options", on_delete=models.CASCADE)
    number = models.IntegerField("Номер ответа")
    content = models.TextField("Содержание варианта теста")
