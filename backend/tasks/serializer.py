from rest_framework import serializers
from .models import Task, Variant, Variable


class VariableSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для переменной
    """
    class Meta:
        model = Variable
        exclude = ('id', 'variant')


class VariantSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для варианта задания
    """
    variables = VariableSerializer(many=True)

    class Meta:
        model = Variant
        exclude = ('id', 'task')


class CreateTaskSerializer(serializers.ModelSerializer):
    """
    Сериализатор создания задачи
    """
    variants = VariantSerializer(many=True)

    def create(self, validated_data):
        # из объекта задания достанем  варианты
        # и создадим объект задания без переменных
        variants_data = validated_data.pop('variants')
        task = Task.objects.create(**validated_data)

        for variant_data in variants_data:
            # из объекта варианта достанем переменные
            # и создадим объект варианта без переменных

            variables_data = variant_data.pop('variables')
            variant = Variant.objects.create(task=task, **variant_data)

            for variable_data in variables_data:
                # создатим объект переменной
                Variable.objects.create(variant=variant, **variable_data)

        return task

    class Meta:
        model = Task
        fields = ('title', 'grade', 'content', 'variants')


class PreviewTaskSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для задачи без подробностей
    """
    class Meta:
        model = Task
        fields = ('title', 'grade', 'withAnswer')


class DetailTaskSerializer(serializers.ModelSerializer):
    """
    Подробный сериализатор задачи
    """
    variants = VariantSerializer(many=True)

    class Meta:
        model = Task
        fields = '__all__'
