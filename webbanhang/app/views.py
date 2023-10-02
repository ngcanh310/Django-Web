from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home (request):
    context = {}
    return render(request, 'app/home.html', context)

def backup(request):
    context = {}
    return render(request, 'app/backup.html', context)

def check(request):
    context = {}
    return render(request, 'app/check.html', context)

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'app/register.html', context)