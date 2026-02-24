from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm,UserUpdateForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('store:home')
        else:
            messages.error(request,'Invalid username or password')
            return render(request, 'users/login.html', {'form': form})
    else:
        context = {'form': LoginForm()}
        return render(request,'users/login.html',context)

@login_required
def user_logout(request):
    logout(request)
    return redirect('store:home')

@login_required
def user_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('users:profile')
    else:
        form = UserUpdateForm(instance=request.user)
    context = {'form': form}
    return render(request, 'users/profile.html', context)

