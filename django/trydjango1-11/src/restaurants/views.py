from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import RestaurantCreateForm
from .models import Restaurant


class RestaurantCreateView(LoginRequiredMixin, CreateView):
    form_class = RestaurantCreateForm
    template_name = 'form.html'
    success_url = '/restaurants'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user  # not the best, should be in pre_save
        return super(RestaurantCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Restaurant'
        return context


class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
    form_class = RestaurantCreateForm
    template_name = 'restaurants/detail-update.html'
    success_url = '/restaurants'

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Update Restaurant'
        return context

    def get_queryset(self):
        return Restaurant.objects.filter(owner=self.request.user)


class RestaurantListView(LoginRequiredMixin, ListView):
    template_name = 'restaurants/restaurants_list.html'

    def get_queryset(self):
        return Restaurant.objects.filter(owner=self.request.user)


class RestaurantDetailView(LoginRequiredMixin, DetailView):
    queryset = Restaurant.objects.all()

