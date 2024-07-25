from django.urls import path
from coag import views

urlpatterns = [
    path('',views.coag_index, name='coag_index'),
    path('<str:drugName>/',views.coag_detail, name='coag_detail'),
]