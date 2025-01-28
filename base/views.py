from django.shortcuts import render, redirect, HttpResponse
from .models import Item
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm, CustomLoginForm, AddItemForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required
def home(request):
    items = Item.objects.all()
    return render(request, 'base/home.html', {'items':items})

@login_required
def my_items(request):
    items = Item.objects.filter(seller=request.user)
    return render(request, 'base/my_products.html', {'items':items})



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
    user = request.user
    liked_items_count = Item.objects.filter(liked=user).count()
    my_items_count = Item.objects.filter(seller=user).count()

    return render(request, "base/profile.html", {"liked_items_count": liked_items_count, "my_items_count":my_items_count })

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

@login_required
def liked(request):
    user = request.user
    liked_items = Item.objects.filter(liked=user)

    return render(request, 'base/liked.html', {'liked_items': liked_items})

@login_required
def upload(request):
    form = AddItemForm()

    if request.method == "POST":
        form = AddItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.seller = request.user

            print(request.FILES)

            if 'picture' in request.FILES:
                print("File is here!")
                item.picture = request.FILES['picture']

            item.save()
            return redirect('home')

    return render(request, 'base/upload.html', {"form": form})


@login_required
def delete(request, pk):
    item=Item.objects.get(id=pk)
    item.delete()

    return redirect('home')


@login_required
def edit(request, pk):
    # Fetch the existing item instance
    item =  Item.objects.get(id=pk)

    # Initialize the form with the item instance
    form = AddItemForm(request.POST or None, request.FILES or None, instance=item)

    if request.method == "POST" and form.is_valid():
        # Set the seller to the current user
        item = form.save(commit=False)
        item.seller = request.user

        if 'picture' in request.FILES:
            item.picture = request.FILES['picture']
        else:
            item.picture = item.picture

        item.save()

        return redirect('home')

    return render(request, 'base/edit.html', {"form": form, "item": item})

