# chat/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import ChatRoom, Message
from .forms import ChatRoomForm
import logging

logger = logging.getLogger(__name__)

@login_required
def lobby(request):
    rooms = ChatRoom.objects.all()
    logger.debug(f'Rooms: {rooms}')  # 추가된 로깅
    return render(request, 'chat/lobby.html', {'rooms': rooms})

@login_required
def create_room(request):
    if request.method == 'POST':
        form = ChatRoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.owner = request.user
            room.save()
            return redirect('chat_room', room_name=room.name)
    else:
        form = ChatRoomForm()
    return render(request, 'chat/create_room.html', {'form': form})

@login_required
def chat_room(request, room_name):
    room = get_object_or_404(ChatRoom, name=room_name)
    if request.method == 'POST':
        message = request.POST.get('message')
        if message:
            Message.objects.create(room=room, user=request.user, content=message)
    messages = room.messages.order_by('timestamp')
    return render(request, 'chat/room.html', {'room': room, 'messages': messages})

@login_required
def leave_room(request, room_name):
    room = get_object_or_404(ChatRoom, name=room_name)
    if room.owner == request.user:
        room.delete()
    else:
        room.messages.filter(user=request.user).delete()
    return redirect('lobby')

@login_required
def delete_room(request, room_name):
    room = get_object_or_404(ChatRoom, name=room_name)
    if room.owner == request.user:
        room.delete()
        return redirect('lobby')
    else:
        return HttpResponseForbidden("You are not allowed to delete this room.")