from django.contrib import admin
from .models import Task, Variant, Variable, Category


class VariantInline(admin.TabularInline):
    model = Variant
    extra = 3


class VariableInline(admin.TabularInline):
    model = Variable
    extra = 2


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    inlines = [VariantInline]


@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    inlines = [VariableInline]


@admin.register(Variable)
class VariantVariableAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
