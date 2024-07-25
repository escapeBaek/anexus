from django.urls import path
from calculator import views

urlpatterns=[
    path('',views.calculator, name='calculator'),
]