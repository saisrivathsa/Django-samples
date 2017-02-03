from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
#for authentication uses
from django.contrib import auth
# for new user
from django.contrib.auth.models import User


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

def sign_up(request):
    return render(request, 'auth_model/create_new_user.html')

def create_new_user(request) :
    try:
        user = User.objects.create_user(
        username = request.POST['username'],
        password = request.POST['password'],
        email = request.POST['email'],
        )
        user.extra_fields = {'phone_number' : request.POST['phone_number']}
        user.save()
        username = request.POST.get('username', '' )
        password = request.POST.get('password', '' )
        user = auth.authenticate( username=username, password=password )
        return HttpResponse('<h2>Created new user %s </h2><br><a href="../signup/">  create another account?</a>' %user.username)
    except :
        return render( request, 'auth_model/create_new_user.html', {'error':'Error making account. Try again'} )
