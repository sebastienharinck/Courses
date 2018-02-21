from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .forms import RestaurantCreateForm
from .models import Restaurant


class RestaurantCreateView(LoginRequiredMixin, CreateView):
    form_class = RestaurantCreateForm
    template_name = 'restaurants/form.html'
    success_url = '/restaurants'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user  # not the best, should be in pre_save
        return super(RestaurantCreateView, self).form_valid(form)


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

