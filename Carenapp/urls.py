from django.conf import settings
from django.contrib import admin
from django.urls import path
from .import  views
from .views import makeappointmentTemplateView, ManageAppointmentTemplateView,patienthomeView,doctorviewappointment,patientviewappointments


urlpatterns = [
path('',views.index, name="index"),
path('contact.html',views.contact, name="contact"),
path('about.html',views.about, name="about"),
path('services.html', views.services, name="services"),
path('nutritionist.html', views.nutritionist, name="nutritionist"),
path('training.html', views.training, name="training"),
path('register/', views.register, name="register"),
path('login.html', views.login, name="login"),
path('logout.html', views.logout, name="logout"),
path('adminviewDoctors/', views.adminviewDoctors, name="adminviewDoctors"),
path('adminviewappointments/', views.adminviewappointments, name="adminviewappointments"),
path('adminaddreceptionist/', views.adminviewappointments, name="adminaddreceptionist"),
path('patienthomeView/', views.patienthomeView, name="patienthomeView"),
path('doctorviewappointment/', views.doctorviewappointment, name="doctorviewappointment"),
path('adminadddoctor/', views.adminadddoctor, name="adminadddoctor"),
path('profile/',views.profile, name="profile"),
path("makeappointment.html",makeappointmentTemplateView.as_view(), name="makeappointment"),
path("manage-appointments/", ManageAppointmentTemplateView.as_view(), name="manage"),
path('patientviewappointments/', views.patientviewappointments, name="patientviewappointments"),



]
