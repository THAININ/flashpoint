from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import ConsoleForm
from .models import ConsoleModel

# Create your views here.

def home_view(request):
    context = {
        'consoles': ConsoleModel.objects.all()
    }
    return render(request, 'store/home.html', context)


def consoles_view(request:HttpRequest):
    if request.method == 'POST':
        formulario = ConsoleForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('store:home')
    context = {
        'form':ConsoleForm
    }
    return render(request, 'store/consoles.html', context)
