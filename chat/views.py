# chat/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ChatRoom, ChatMessage
from .forms import ChatRoomForm
from django.contrib.auth import get_user_model
from django.http import HttpResponseForbidden

User = get_user_model()

@login_required
def chat_room_list(request):
    user_rooms = ChatRoom.objects.filter(user1=request.user) | ChatRoom.objects.filter(user2=request.user)
    return render(request, 'chat/chat_room_list.html', {'rooms': user_rooms})

@login_required
def create_chat_room(request):
    if request.method == 'POST':
        form = ChatRoomForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            other_user = get_object_or_404(User, username=username)
            if ChatRoom.objects.filter(user1=request.user, user2=other_user).exists() or \
               ChatRoom.objects.filter(user1=other_user, user2=request.user).exists():
                room = ChatRoom.objects.get((models.Q(user1=request.user) & models.Q(user2=other_user)) | \
                                            (models.Q(user1=other_user) & models.Q(user2=request.user)))
            else:
                room = ChatRoom.objects.create(user1=request.user, user2=other_user)
            return redirect('chat_room', room_id=room.id)
    else:
        form = ChatRoomForm()
    return render(request, 'chat/chat_room_list.html', {'form': form})

@login_required
def chat_room(request, room_id):
    room = get_object_or_404(ChatRoom, id=room_id)
    if request.user != room.user1 and request.user != room.user2:
        return HttpResponseForbidden("You do not have permission to access this chat room.")
    
    if request.method == 'POST':
        message = request.POST.get('message')
        if message:
            ChatMessage.objects.create(room=room, author=request.user, message=message)
    
    messages = room.messages.order_by('timestamp')
    return render(request, 'chat/room.html', {'room': room, 'messages': messages})

@login_required
def clear_chat(request, room_id):
    chat_room = get_object_or_404(ChatRoom, id=room_id)
    if request.user != chat_room.user1 and request.user != chat_room.user2:
        return HttpResponseForbidden("You do not have permission to clear this chat.")
    
    ChatMessage.objects.filter(room=chat_room).delete()
    return redirect('chat_room', room_id=room_id)
