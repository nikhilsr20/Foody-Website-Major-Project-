

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import Register  # your RegisterForm
# from django.http import HttpResponseRedirect  (not needed now)

def register(request):
    if request.method == "POST":
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # ✅ Use URL name or path
    else:
        form = Register()

    return render(request, 'authentication/Register.html', {'form': form})
