from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def pay_view(request):
    return render(request, 'payments/payments.html')