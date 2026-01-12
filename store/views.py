from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import ConsoleForm

# Create your views here.

def home_view(request):
    return render(request, 'store/home.html')


def consoles_view(request:HttpRequest):
    if request.method == 'POST':
        formulario = ConsoleForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('store:consoles')
    context = {
        'form':ConsoleForm
    }
    return render(request, 'store/consoles.html', context)
