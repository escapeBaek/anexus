from django.shortcuts import render, get_object_or_404
from .models import Exam, Question, ExamResult, Category
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from accounts.decorators import user_is_specially_approved
import json

@login_required
@user_is_specially_approved
def exam_landing_page(request):
    return render(request, 'exam/landing_page.html')

@login_required
@user_is_specially_approved
def exam_list(request):
    exams = Exam.objects.all()
    return render(request, 'exam/exam_list.html', {'exams': exams})

@login_required
@user_is_specially_approved
def exam_detail(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)
    return render(request, 'exam/exam_detail.html', {'exam': exam})

@login_required
@user_is_specially_approved
def question_list(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)
    questions = exam.questions.all().order_by('order')

    # Format the comment for readability, ensuring line breaks are retained
    for question in questions:
        question.comment = question.comment.replace('\n', '<br>')

    return render(request, 'exam/question_list.html', {
        'exam': exam,
        'questions': questions
    })

@login_required
@user_is_specially_approved
def save_exam_results(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        # exam_id는 question_list.html(Exam 기반)에서 사용
        exam_id = data.get('exam_id', None)

        # category_name은 category_questions.html(카테고리 기반)에서 사용
        category_name = data.get('category_name', None)

        num_correct = data.get('num_correct', 0)
        num_incorrect = data.get('num_incorrect', 0)
        num_unanswered = data.get('num_unanswered', 0)
        num_noanswer = data.get('num_noanswer', 0)
        detailed_results = data.get('detailed_results', [])

        user = request.user
        exam_instance = None

        # exam_id가 넘어온 경우 → Exam 기반 결과
        if exam_id is not None:
            exam_instance = get_object_or_404(Exam, id=exam_id)

        # ExamResult 생성 (exam이 없으면 None으로 저장됨)
        result = ExamResult.objects.create(
            user=user,
            exam=exam_instance,          # nullable
            category_name=category_name, # 카테고리명 저장
            num_correct=num_correct,
            num_incorrect=num_incorrect,
            num_unanswered=num_unanswered,
            num_noanswer=num_noanswer,
            detailed_results=detailed_results,
        )

        return JsonResponse({'status': 'ok', 'result_id': result.id})
    else:
        return JsonResponse({'status': 'error'}, status=400)

@login_required
@user_is_specially_approved
def exam_results(request):
    result_id = request.GET.get('result_id')
    # 현재 로그인한 사용자와 result_id가 일치하는지 확인
    result = get_object_or_404(ExamResult, id=result_id, user=request.user)
    return render(request, 'exam/exam_results.html', {'result': result})

@login_required
@user_is_specially_approved
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'exam/category_list.html', {'categories': categories})

@login_required
@user_is_specially_approved
def category_questions(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    questions = Question.objects.filter(category=category).order_by('order')
    return render(request, 'exam/category_questions.html', {
        'category_name': category.name,
        'questions': questions
    })
