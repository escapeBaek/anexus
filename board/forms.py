# board/forms.py

from django import forms
from .models import Board, Comment
from ckeditor.widgets import CKEditorWidget

class BoardForm(forms.ModelForm):
    contents = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Board
        fields = ['title', 'contents']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a comment...'}),
        }
