from rest_framework import serializers
from tasks.models import TestTask, OptionForTestTask


class OptionForTestTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionForTestTask
        fields = "__all__"


class TestTaskContentSerializer(serializers.ModelSerializer):
    options = OptionForTestTaskSerializer(many=True)

    class Meta:
        model = TestTask
        fields = ('id', 'answer', 'text', 'options', )
