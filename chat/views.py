# chat/views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

def chat_room_list(request):
    User = get_user_model()
    users = User.objects.all()  # 모든 사용자 가져오기
    return render(request, 'chat/chat_room_list.html', {'users': users})


def chat_with_user(request, username):
    User = get_user_model()
    try:
        other_user = User.objects.get(username=username)
    except User.DoesNotExist:
        other_user = None

    if other_user:
        room_name = f'chat_{request.user.username}_{other_user.username}'
        return render(request, 'chat/room.html', {'other_user': other_user, 'room_name': room_name})
    else:
        room_name = f'chat_{request.user.username}_offline'
        message = "The user does not exist or is not logged in"
        return render(request, 'chat/room.html', {'message': message, 'room_name': room_name})


@login_required
def chat_room(request, room_name):
    return render(request, 'chat/room.html', {'room_name': room_name})
