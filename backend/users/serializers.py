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


class UserSerializer(serializers.ModelSerializer):
    """
    Создание пользователя
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = (
            "first_name", "last_name", "username", "email", "password", "is_creator"
        )
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'is_creator': {'required': True}
        }

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        return user


