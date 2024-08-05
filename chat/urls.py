# chat/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lobby, name='lobby'),
    path('create/', views.create_room, name='create_room'),
    path('leave/<str:room_name>/', views.leave_room, name='leave_room'),
    path('delete/<str:room_name>/', views.delete_room, name='delete_room'),  # delete_room URL 추가
    path('<str:room_name>/', views.chat_room, name='chat_room'),
]
