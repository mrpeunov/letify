from rest_framework import serializers
from .models import Task, Variant, Variable, Category


class CategorySerializer(serializers.ModelSerializer):
    """Сериалайзер для категории"""

    class Meta:
        model = Category
        fields = '__all__'


class AddCategorySerializer(serializers.ModelSerializer):
    """Сериалайзер для категории"""

    class Meta:
        model = Category
        fields = ('title', )


class VariableSerializer(serializers.ModelSerializer):
    """Сериалайзер для переменной"""

    class Meta:
        model = Variable
        exclude = ('id', 'variant')


class VariantSerializer(serializers.ModelSerializer):
    """Сериалайзер для варианта задания"""
    variables = VariableSerializer(many=True)

    def create_or_update(self, task, validated_data):
        """Создание или обнолвение вариантов задания"""
        if 'variables' in validated_data:
            variables_data = validated_data.pop('variables')
            for variable_data in variables_data:
                variable, _ = Variable.objects.get_or_create(variant=task, variable=variable_data.get("variable"))
                VariableSerializer().update(variable, variable_data)

        return super(VariantSerializer, self).update(task, validated_data)

    class Meta:
        model = Variant
        exclude = ('task', 'id')


class CreateUpdateTaskSerializer(serializers.ModelSerializer):
    """Сериализатор создания и обновления задачи"""
    variants = VariantSerializer(many=True)

    def create(self, validated_data):
        variants_data = validated_data.pop('variants')  # из данных объекта убираются варианты
        print(validated_data)
        task = super(CreateUpdateTaskSerializer, self).create(validated_data)  # по данным создается задание
        self.update_variants_for_task(task, variants_data)  # для этого задания обновляются варианты
        return task

    def update(self, task, validated_data):
        variants_data = validated_data.pop('variants')  # из данных объекта убираются варианты
        self.update_variants_for_task(task, variants_data)  # для задания обновляются варианты
        return super(CreateUpdateTaskSerializer, self).update(task, validated_data)  # по данным обнолвяется задание

    def update_variants_for_task(self, task, variants_data):
        for variant_data in variants_data:
            variant, _ = Variant.objects.get_or_create(task=task, number=variant_data.get("number"))
            VariantSerializer().create_or_update(variant, variant_data)

    class Meta:
        model = Task
        fields = ('title', 'grade', 'content', 'variants', 'category')


class DetailTaskSerializer(serializers.ModelSerializer):
    """
    Подробный сериализатор задачи
    """
    variants = VariantSerializer(many=True)

    class Meta:
        model = Task
        fields = '__all__'


class PreviewTaskSerializer(serializers.ModelSerializer):
    """Сериалайзер для задачи без подробностей"""
    class Meta:
        model = Task
        fields = ('id', 'title', 'grade', 'withAnswer')


class CategorySerializer(serializers.ModelSerializer):
    tasks = PreviewTaskSerializer(many=True)

    class Meta:
        model = Category
        fields = ('id', 'title', 'tasks')
