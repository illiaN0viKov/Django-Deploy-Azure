from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.home, name="home"),

    path("register/", views.register, name="register"),

    path("login/", views.login, name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path("profile/", views.profile, name="profile"),

    path("overview/<int:pk>/", views.item_overview, name="overview"),
    path('toggle_like/<int:pk>/', views.toggle_like, name='toggle_like'),

    path ('liked/', views.liked, name="liked"),
    
    path ('add/', views.upload, name="upload"),

    path ('delete/<str:pk>/', views.delete, name="delete"),

    path ('edit/<str:pk>/', views.edit, name="edit"),

    path ('my-added-items', views.my_items, name="my-added-items"),
    
]
