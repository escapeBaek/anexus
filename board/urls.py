from django.urls import path
from board import views

urlpatterns = [
    path('', views.board_index, name='board_index'),
    path('<int:pk>/', views.board_detail, name='board_detail'),
]