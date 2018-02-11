import random

from django.shortcuts import render
from django.views import View

def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html', {})
