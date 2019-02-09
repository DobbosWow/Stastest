from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegUserForm

def index(request):
    return render(request, 'registr/index.html')

def regform(request):
    if request.method=="POST":
        form = RegUserForm(request.POST)
        if form.is_valid():
            newuser = form.save(commit=False)
            newuser.save()
            return redirect('regform')
    else:
        form = RegUserForm()
    return render(request, 'registr/regform.html', {'form': form})
        

    
