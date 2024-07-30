from django import forms
from .models import Board
from ckeditor.widgets import CKEditorWidget

class BoardForm(forms.ModelForm):
    contents = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Board
        fields = ['title', 'contents']
