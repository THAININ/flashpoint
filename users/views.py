from django.shortcuts import render

# Create your views here.

def user_page_view(request):
    return render(request, 'users/user_page.html')