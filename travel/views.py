from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    name = "Bob"
    context = {'name': 'Dave'}
    return render(request, 'home.html', context)