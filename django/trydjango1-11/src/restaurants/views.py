from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .forms import RestaurantCreateForm
from .models import Restaurant


def restaurant_createview(request):
    form = RestaurantCreateForm(request.POST or None)
    erros = None
    if form.is_valid():
        obj = Restaurant.objects.create(
            name=form.cleaned_data.get('name'),
            location=form.cleaned_data.get('location'),
            category=form.cleaned_data.get('category')
        )
        return HttpResponseRedirect('/restaurants')
    else:
        errors = form.errors

    template_name = 'restaurants/form.html'
    context = {'form': form, 'errors': errors}
    return render(request, template_name, context)


def restaurant_listview(request):
    template_name = 'restaurants/restaurants_list.html'
    queryset = Restaurant.objects.all()
    context = {
        'object_list': queryset,

    }
    return render(request, template_name, context)


class RestaurantListView(ListView):
    template_name = 'restaurants/restaurants_list.html'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        if slug:
            queryset = Restaurant.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug)
            )
        else:
            queryset = Restaurant.objects.all()
        return queryset


class RestaurantDetailView(DetailView):
    queryset = Restaurant.objects.all()

