from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Restaurant


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

    def get_context_data(self, *args, **kwargs):
        print(kwargs)
        context = super(RestaurantDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context
