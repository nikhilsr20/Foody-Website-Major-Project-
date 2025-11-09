

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import Register,Login
from django.contrib.auth import authenticate,login

from django.contrib.auth import logout
def register(request):
    if request.method == "POST":
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = Register()

    return render(request, 'authentication/Register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        
        form = Login(request=request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print("validd")
            # here i changes the authenticate function and write it in backend.py file
            user = authenticate(request, username=email, password=password)
            print(user)

            if user is not None:
                login(request, user)  
                return redirect('home')
        else:
           
            print(form.errors)    
    else:
        form = Login()
    return render(request, 'authentication/login.html', {'form': form})


def logout_view(request):
    logout(request)           
    return redirect('home') 