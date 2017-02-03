from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
#for authentication uses
from django.contrib import auth


def login(request) :
    return render(request, 'auth_model/login.html')

def logout(request) :
    auth.logout(request)
    return HttpResponseRedirect(reverse('auth_model:login'))

def success(request) :
    return render(request, 'auth_model/success.html', {'username' :request.user.username})

def auth_view(request) :
    username = request.POST.get('username', '' )
    password = request.POST.get('password', '' )
    user = auth.authenticate( username=username, password=password )

    if user is not None :
        auth.login( request, user)
        return HttpResponseRedirect(reverse("auth_model:success"))
    else :
        return render(request, "auth_model/login.html", {'error':'Invalid Credentials'})
        #return HttpResponseRedirect(reverse("auth_model:login", kwargs={'error' : 'Invalid Credentials
