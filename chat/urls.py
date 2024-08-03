# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_room_list, name='chat_room_list'),
    path('chat/<str:username>/', views.chat_with_user, name='chat_with_user'),
]
