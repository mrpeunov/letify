from datetime import datetime

from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token
from users.models import CustomUser


def login(username, email, password):
    if username is None:
        username = CustomUser.objects.get(email=email).username

    user = authenticate(username=username, password=password)

    if not user:
        raise ObjectDoesNotExist

    token, _ = Token.objects.get_or_create(user=user)

    return token
