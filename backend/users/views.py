from django.http import HttpResponse
from django.shortcuts import render


def login():
    return HttpResponse("login", status=200)


def logout():
    return HttpResponse("logout", status=200)


def register():
    return HttpResponse("register", status=200)
