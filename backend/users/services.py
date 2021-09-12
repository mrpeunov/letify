from datetime import datetime

from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token


def login(username, email, password):
    user = authenticate(username=username, password=password)

    if not user:
        raise ObjectDoesNotExist

    token, _ = Token.objects.get_or_create(user=user)

    user.last_login = datetime.now()
    user.save()

    return token
