from django.contrib import admin
from django.urls import path
from portfolio import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contacts, name='contacts'),
    path('project/', views.project, name='project'),
    path('resume/', views.resume, name='resume'),
]
