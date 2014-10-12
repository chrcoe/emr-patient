from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login

def login(request):
    state = "Please enter Username and Password"
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "Logged in."
            else:
                state = "Account is not active. Contact your system administrator."
        else:
            state = "Your username and/or password were incorrect."

    return render_to_response('main/base-login.html',{'state':state, 'username': username})
