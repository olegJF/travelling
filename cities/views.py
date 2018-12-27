from django.shortcuts import render
from .models import City

def home(request):
    cities = City.objects.all()
    return render(request, 'cities/home.html', {'objects_list': cities})