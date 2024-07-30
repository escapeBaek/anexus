from django.urls import path
from board import views

urlpatterns = [
    path('', views.board_index, name='board_index'),
    path('<int:pk>/', views.board_detail, name='board_detail'),
    path('create/', views.board_create, name='board_create'),  # 새로운 URL 패턴 추가
]
