from django.contrib import admin
from .models import Task, Variant, VariantVariable


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    pass


@admin.register(VariantVariable)
class VariantVariableAdmin(admin.ModelAdmin):
    pass
