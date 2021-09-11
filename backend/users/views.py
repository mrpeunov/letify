from django.http import HttpResponse
from django.shortcuts import render


def login(request):
    return HttpResponse("login", status=200)


def logout(request):
    return HttpResponse("logout", status=200)


def register(request):
    """
    Приходит:
     +username,
     +email,
     +password,
     +firstname,
     +lastname,
     isCreator,
     group,
    """
    return HttpResponse("register", status=200)
