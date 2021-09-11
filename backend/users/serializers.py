from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from users.models import CustomUser, Group


# class CreateUserSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = CustomUser
#         fields = ("login", "email", "password")
#
#     def create(self, validated_data):
#         user = super(CreateUserSerializer, self).create(validated_data)
#         user.set_password(validated_data['password'])
#         user.save()
#         return user


class StudentUserSerializer(serializers.ModelSerializer):
    """
    Создание пользователя, который не может создавать задания
    """
    password = serializers.CharField(write_only=True)
    group = serializers.CharField(required=False)

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data.get('username'),
            password=validated_data.get('password'),
            email=validated_data.get('email'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            is_creator=False
        )

        group_title = validated_data.get('group')
        if group_title:
            user.group, created = Group.objects.get_or_create(title=validated_data['group'])
            user.save()

        return user

    class Meta:
        model = CustomUser
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
            "group",
        )
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
        }
