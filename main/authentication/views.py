

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import Register,Login
from django.contrib.auth import authenticate,login
def register(request):
    if request.method == "POST":
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = Register()

    return render(request, 'authentication/Register.html', {'form': form})


def login(request):
    if request.method == "POST":
        form = Login(request=request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)  
                return redirect('home')
    else:
        form = Login()
    return render(request, 'authentication/login.html', {'form': form})