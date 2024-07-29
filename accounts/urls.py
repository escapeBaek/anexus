from django.contrib import admin
from django.urls import path
from .views import login_view, register
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', views.register, name='register'),
]