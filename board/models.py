from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.conf import settings

# Create your models here.
class Board(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    title = models.CharField(max_length=255, default='default')
    contents = RichTextField(default='default')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    
    def save(self, *args, **kwargs):
        if self.id is None:  # 새로운 인스턴스인 경우
            last_entry = Board.objects.order_by('id').last()
            if last_entry:
                self.id = last_entry.id + 1
            else:
                self.id = 1  # 첫 번째 글의 경우 ID는 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
