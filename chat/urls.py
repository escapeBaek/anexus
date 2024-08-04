# chat/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_room_list, name='chat_room_list'),
    path('create_chat_room/', views.create_chat_room, name='create_chat_room'),
    path('<int:room_id>/', views.chat_room, name='chat_room'),
    path('clear_chat/<int:room_id>/', views.clear_chat, name='clear_chat'),
]
