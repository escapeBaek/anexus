from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from board.models import Board

class BoardAdmin(SummernoteModelAdmin):
    summernote_fields = ('contents',)
    list_display = ('title', 'author', 'created_date', 'modified_date')

admin.site.register(Board, BoardAdmin)