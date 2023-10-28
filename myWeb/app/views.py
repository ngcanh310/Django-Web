from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def home (request):
    tours = Tour.objects.all() 
    foods = Food.objects.all()
    specials = Special.objects.all()
    context = {'tours': tours, 'foods' : foods, 'specials':specials}
    return render(request, 'app/home.html', context)

def backup(request):
    id = request.GET.get("id", "")
    tours = Tour.objects.filter(id = id)
    context = {'tours': tours}
    return render(request, 'app/backup.html', context)

def backupFood(request):
    id = request.GET.get("id", "")
    foods = Food.objects.filter(id = id)
    context = {'foods': foods}
    return render(request, 'app/backupFood.html', context)

def check(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'User or password is not correct !')
    context = {}
    return render(request, 'app/check.html', context)

def logoutPage(request):
    logout(request)
    return redirect('check')

def register(request):
    form = CreateUser()
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('check')
    context = {'form': form}
    return render(request, 'app/register.html', context)

def listTour(request):
    tours = Tour.objects.all() 
    context = {'tours': tours}
    return render(request, 'app/listTour.html', context)

def listFood(request):
    foods = Food.objects.all() 
    context = {'foods' : foods}
    return render(request, 'app/listFood.html', context)