from django.db import models
from django.conf import settings  # settings.AUTH_USER_MODEL을 사용하기 위해 추가
from django.contrib.auth import get_user_model  # User 모델을 가져오기 위해 추가

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
    order = models.PositiveIntegerField(default=0)  # 문제의 순서를 저장할 필드

    class Meta:
        ordering = ['order']  # 'order' 필드를 기준으로 정렬

    def __str__(self):
        return self.question_text

User = get_user_model()  # 현재 프로젝트에서 사용 중인 사용자 모델을 가져옴

class ExamResult(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    date_taken = models.DateTimeField(auto_now_add=True)
    num_correct = models.IntegerField()
    num_incorrect = models.IntegerField()
    num_unanswered = models.IntegerField()
    num_noanswer = models.IntegerField(default=0)
    detailed_results = models.JSONField()  # 각 문제별 결과를 저장

    def __str__(self):
        return f'{self.user.username} - {self.exam.title} ({self.date_taken})'