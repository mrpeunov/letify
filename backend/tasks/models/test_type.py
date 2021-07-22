from tasks.models.base import AbstractTask


class TestTask(AbstractTask):
    content = models.TextField("Контент задачи")

    def get_all_variants(self):
        pass

    def get_random_variant(self):
        pass

    def check_answer_correctness(self, answer):
        pass
#
#
# class OptionForTest(models.Model):
#     """Варианты задания для тема"""
#     number = models.IntegerField("Номер варианта внутри теста")
#     content = models.TextField("Содержание варианта теста")
