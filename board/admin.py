from django.contrib import admin
from board.models import Board
from django_summernote.admin import SummernoteModelAdmin

class BoardAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    summernote_fields = ('contents',)
    list_display = ('title', 'author', 'created_date', 'modified_date')

admin.site.register(Board, BoardAdmin)
