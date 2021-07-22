from django.contrib import admin
from .models.base import Category, AbstractTask
from tasks.models.default_test import DefaultTask, DefaultTaskVariant, VariableForDefaultTask


# class VariantInline(admin.TabularInline):
#     model = Variant
#     extra = 3
#
#
# class VariableInline(admin.TabularInline):
#     model = Variable
#     extra = 2


@admin.register(VariableForDefaultTask)
class VariableForDefaultTaskAdmin(admin.ModelAdmin):
    pass


@admin.register(DefaultTaskVariant)
class DefaultTaskVariantAdmin(admin.ModelAdmin):
    pass


@admin.register(DefaultTask)
class DefaultTaskAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
