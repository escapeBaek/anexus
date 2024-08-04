# chat/forms.py
from django import forms
from .models import ChatRoom

class ChatRoomForm(forms.Form):
    username = forms.CharField(max_length=150, label='Enter Username')
