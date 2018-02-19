from django.shortcuts import render

from .models import Restaurant


def restaurant_listview(request):
    template_name = 'restaurants/restaurants_list.html'
    queryset = Restaurant.objects.all()
    context = {
        'object_list': queryset,

    }
    return render(request, template_name, context)