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
    path('toggle_like/<int:pk>/', views.toggle_like, name='toggle_like')
    
]
