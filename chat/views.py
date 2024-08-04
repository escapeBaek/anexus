# chat/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import ChatRoom, ChatMessage
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def chat_room_list(request):
    users = User.objects.all()  # 모든 사용자 가져오기
    return render(request, 'chat/chat_room_list.html', {'users': users})

@login_required
def chat_with_user(request, username):
    other_user = get_object_or_404(User, username=username)
    room_name = f'chat_{request.user.username}_{other_user.username}'
    room, created = ChatRoom.objects.get_or_create(name=room_name)

    if request.method == 'POST':
        message_content = request.POST.get('message')
        if message_content:
            ChatMessage.objects.create(room=room, author=request.user, content=message_content)
            return redirect('chat_with_user', username=username)

    messages = room.messages.all()

    return render(request, 'chat/room.html', {
        'other_user': other_user,
        'room_name': room_name,
        'messages': messages,
    })

@login_required
def clear_chat_room(request, room_name):
    room = get_object_or_404(ChatRoom, name=room_name)
    if room.messages.filter(author=request.user).exists() or request.user.is_superuser:
        room.messages.all().delete()
    return redirect('chat_with_user', username=room_name.split('_')[1])
