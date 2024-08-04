from django.contrib import admin
from .models import Room, Message  # 모델 이름 확인

admin.site.register(Room)
admin.site.register(Message)
