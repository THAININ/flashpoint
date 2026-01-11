from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def home_view(request):
    return render(request, 'store/home.html')


def consoles_view(request):
    return render(request, 'store/consoles.html')
