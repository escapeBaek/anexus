from django.db import models

# Create your models here.
class Exam(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    image = models.ImageField(upload_to='question_images/', blank=True, null=True)
    option1 = models.CharField(max_length=200, default='default')
    option2 = models.CharField(max_length=200, default='default')
    option3 = models.CharField(max_length=200, default='default')
    option4 = models.CharField(max_length=200, default='default')
    option5 = models.CharField(max_length=200, default='default')
    correct_option = models.CharField(max_length=200, default='default')
    comment = models.TextField(default='default')
    comment_image = models.ImageField(upload_to='question_images/', blank=True, null=True)

    def __str__(self):
        return self.question_text