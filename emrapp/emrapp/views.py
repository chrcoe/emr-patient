from django.http import HttpResponse
from django.shortcuts import render


def login(request):
    return render(request, 'main/login.html',
                  {'page_name': 'LOGIN'})
