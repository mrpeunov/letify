from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from rest_framework import permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import CustomUser
from users.serializers import UserSerializer


# общий логин
# общий выход из системы
# регистрация
# забыли пароль
# поменять пароль
from users.services import login


class RegistrationView(CreateAPIView):
    """
    Регистрация пользователей
    """
    model = CustomUser
    permission_classes = (permissions.AllowAny, )
    serializer_class = UserSerializer


class LoginView(APIView):
    """
    Вход в систему
    """
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")

        if (username is None and email is None) or password is None:
            return Response(
                {'error': 'Please provide both username and password'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            token = login(username, email, password)
            return Response(
                {'token': token.key},
                status=status.HTTP_200_OK
            )
        except ObjectDoesNotExist:
            return Response(
                {'error': 'Invalid Credentials'},
                status=status.HTTP_400_BAD_REQUEST
            )


class LogoutView(APIView):
    """
    Выход из системы
    """
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response(
                {'test': 'Success logout'},
                status=status.HTTP_204_NO_CONTENT
            )
        except ObjectDoesNotExist:
            return Response(
                {'error': 'Object dot found'},
                status=status.HTTP_400_BAD_REQUEST
            )
