from django.shortcuts import render, get_object_or_404
from .models import Exam, Question
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def exam_list(request):
    exams = Exam.objects.all()
    return render(request, 'exam/exam_list.html', {'exams': exams})

def exam_detail(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)
    return render(request, 'exam/exam_detail.html', {'exam': exam})

def question_list(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)
    questions = exam.questions.all()
    return render(request, 'exam/question_list.html', {'exam': exam, 'questions': questions})


# 답변 return
def submit_answers(request):
    if request.method == 'POST':
        # 여기에 답변 처리 로직을 구현합니다.
        # 예: 사용자가 선택한 답변을 저장하거나, 점수를 계산합니다.

        return HttpResponseRedirect(reverse('some_result_page'))
    else:
        # 비정상적인 접근 처리
        return HttpResponseRedirect(reverse('exam_list'))