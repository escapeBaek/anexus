from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.conf import settings

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=255, default='default')
    contents = RichTextField(default='default')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
