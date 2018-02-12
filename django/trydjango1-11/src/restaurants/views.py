import random

from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

class ContactView(View):
    def get(self, request, *args, **kwargs):
        print(kwargs)
        return render(request, 'contact.html', {})

class ContactTemplateView(TemplateView):
    template_name = 'contact.html'

    def get(self, request, *args, **kwargs):
        print(kwargs)
        return render(request, 'contact.html', {})