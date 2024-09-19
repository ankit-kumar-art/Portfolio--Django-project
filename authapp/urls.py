
from django.contrib import admin
from django.urls import path
from authapp import views

urlpatterns = [
    path('signup/',views.signup),
    path('login/',views.login),
    path('logout/',views.logout),
]

