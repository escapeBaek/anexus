from django.db import models
from django.utils import timezone

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=255, default='default')
    contents = models.TextField(default='default')
    author = models.CharField(max_length=500, default='default')
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title