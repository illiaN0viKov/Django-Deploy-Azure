from django.shortcuts import render, redirect, HttpResponse
from .models import Item
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm, CustomLoginForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required
def home(request):
    items = Item.objects.all()
    return render(request, 'base/home.html', {'items':items})


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = CustomUserCreationForm() 

    return render(request, 'base/register.html', {'form': form})


def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = CustomLoginForm()
    if request.method == "POST":
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')  

    return render(request, 'base/login.html', {'form': form})


@login_required
def profile(request):
    return render(request, "base/profile.html")

@login_required
def item_overview(request, pk):
    item = Item.objects.get(pk=pk) 
    return render(request, 'base/overview.html', {'item': item})
    

@login_required
def toggle_like(request, pk):
    item = Item.objects.get(pk=pk) 

    if request.user in item.liked.all():
        item.liked.remove(request.user)
    else:
        item.liked.add(request.user)

    return redirect('overview', pk=pk)