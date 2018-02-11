import random

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    rand = random.randint(0, 1000)
    return render(request, 'base.html', {'random': rand})

def home2(request):
    rand = random.randint(0, 1000)
    return render(request, 'home2.html', {'random': rand})

def home3(request):
    rand = random.randint(0, 1000)
    return render(request, 'home3.html', {'random': rand})