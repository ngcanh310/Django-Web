from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('backup/', views.backup, name="backup"),
    path('register/', views.register, name = "register"),
    path('check/', views.check, name="check"),
    path('logout/', views.logoutPage, name="logout"),
    path('listTour/', views.listTour, name="listTour"),
    path('listFood/', views.listFood, name="listFood"),
    path('backupFood/', views.backupFood, name="backupFood")
]