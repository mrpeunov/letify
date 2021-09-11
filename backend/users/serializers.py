from rest_framework import serializers
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
    group = serializers.CharField()

    def create(self, validated_data):

        # group_title = validated_data.pop['group']

        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_creator=False
        )
        # if group_title:
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
