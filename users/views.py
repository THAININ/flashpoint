from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = RegisterForm()
    context = {'form':form}
    return render(request, 'users/register.html',context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return render(request,'store/home.html')
    else:
        context = {'form': LoginForm()}
        return render(request,'users/login.html',context)

@login_required
def user_logout(request):
    logout(request)
    return redirect('users:login')

@login_required
def user_profile(request):
    return render(request,'users/profile.html')

