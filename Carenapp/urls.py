from django.conf import settings
from django.contrib import admin
from django.urls import path
from .import  views


urlpatterns = [
 path('',views.home, name="home"),
 path('contact.html',views.contact, name="contact"),
 path('about.html',views.about, name="about"),
 path('services.html', views.services, name="services"),
 path('nutritionist.html', views.nutritionist, name="nutritionist"),
 path('training.html', views.training, name="training"),
 path('register/', views.register, name="register"),
 path('login.html', views.login, name="login"),
 path('logout.html', views.logout, name="logout"),

 ]
