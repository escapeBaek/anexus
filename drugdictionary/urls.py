# drugdictionary/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.drug_list, name='drug_list'),
    path('search/', views.search_drug, name='search_drug'),
]
