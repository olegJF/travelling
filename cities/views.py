from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import City

def home(request):
    cities = City.objects.all()
    return render(request, 'cities/home.html', {'objects_list': cities})


class CityDetailView(DetailView):
    queryset = City.objects.all()
    context_object_name = 'object'
    template_name = 'cities/detail.html'
    