from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from users.models import CustomUser
from users.serializers import StudentUserSerializer


def login(request):
    return HttpResponse("login", status=200)


def logout(request):
    return HttpResponse("logout", status=200)


class RegistrationStudentUserView(CreateAPIView):
    model = CustomUser
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StudentUserSerializer

# class CustomAuthToken(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data,
#                                            context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#             'user_id': user.pk,
#             'email': user.email
#         })


@csrf_exempt
def register(request):
    print(request.POST)
    """
    Приходит:
     username,
     email,
     password,
     firstname,
     lastname,
     isCreator,
     group,
    """
    return HttpResponse("register", status=200)
