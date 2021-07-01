from django.contrib import admin
from .models import Competition, Attempt, TaskAnswer


@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    pass


@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    pass


@admin.register(TaskAnswer)
class TaskAnswerAdmin(admin.ModelAdmin):
    pass
