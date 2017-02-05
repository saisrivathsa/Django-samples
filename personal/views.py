from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request) :
    return render(request, 'personal/home.html')

def contact(request) :
    return render(request, 'personal/basic.html', {'content':["please contact me at the given email address", "srivathsaeric@gmail.com"]})
