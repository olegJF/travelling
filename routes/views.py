from django.shortcuts import render
from .forms import *

def home(request):
    form = RouteForm()
    return render(request, 'routes/home.html', {'form': form})
