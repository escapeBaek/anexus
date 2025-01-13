from django.contrib import admin
from .models import Exam, Question, Category

# Register your models here.
admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Category)