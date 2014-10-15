from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext


def login_page(request):
    # check if already logged in, redirect to their dashboard
    if request.user.is_authenticated():
        return redirect('/patient/{}'.format(request.user.id))
    errMsg = ''  # default to no error message
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        patient = authenticate(username=username, password=password)
        if patient is not None:
            if patient.is_active:
                # this handles setting the session info
                login(request, patient)
                # redirect to admin page if is_admin or is_staff
                if patient.is_staff or patient.is_admin:
                    return redirect('/admin/')
                # redirect to dashboard if not staff or admin
                return redirect('/patient/{}'.format(patient.id))
            else:
                errMsg = "Account is not active. Contact your system administrator."
        else:
            errMsg = "Your username and/or password were incorrect."

    context = RequestContext(
        request, {'errMsg': errMsg, 'username': username,
                  'page_name': 'Patient Login'}
    )
    return render_to_response('main/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('/')  # redirects to the login page
