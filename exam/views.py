from django.shortcuts import render, get_object_or_404, reverse
from .models import Exam, Question, ExamResult, Category
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from accounts.decorators import user_is_specially_approved
import json
from django.views.decorators.http import require_POST
from .models import Question,Bookmark

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
    
    # 현재 사용자의 북마크된 질문 ID 목록을 가져옴
    bookmarked_questions = Bookmark.objects.filter(
        user=request.user  # 현재 사용자의 북마크만 필터링
    ).values_list('question_id', flat=True)
    
    # 각 질문에 북마크 상태 추가
    for question in questions:
        question.is_bookmarked = question.id in bookmarked_questions
    
    return render(request, 'exam/question_list.html', {
        'exam': exam,
        'questions': questions,
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
    result = get_object_or_404(ExamResult, id=result_id, user=request.user)

    # 북마크된 질문 ID 가져오기
    bookmarked_questions = set(
        Bookmark.objects.filter(user=request.user).values_list('question_id', flat=True)
    )

    # 모든 질문들을 미리 가져와서 dictionary로 만들기
    all_questions = Question.objects.all()
    question_dict = {q.question_text: q for q in all_questions}

    # detailed_results에 'question_id' 및 'is_bookmarked' 추가
    updated_results = []
    for detail in result.detailed_results:
        question_text = detail.get('question', '')
        question = question_dict.get(question_text)
        
        updated_detail = detail.copy()  # Create a copy of the original detail
        
        if question:
            updated_detail['question_id'] = question.id
            updated_detail['is_bookmarked'] = question.id in bookmarked_questions
        else:
            # 문제를 찾을 수 없는 경우의 처리
            print(f"Question not found: {question_text[:100]}...")
            # DB에서 부분 일치로 검색 시도
            potential_matches = Question.objects.filter(question_text__contains=question_text[:50]).first()
            if potential_matches:
                updated_detail['question_id'] = potential_matches.id
                updated_detail['is_bookmarked'] = potential_matches.id in bookmarked_questions
            else:
                updated_detail['question_id'] = None
                updated_detail['is_bookmarked'] = False
        
        updated_results.append(updated_detail)

    # 업데이트된 결과를 result 객체에 저장
    result.detailed_results = updated_results

    return render(request, 'exam/exam_results.html', {
        'result': result,
    })

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
    
@login_required
@user_is_specially_approved
def bookmarked_questions(request):
    # 현재 사용자의 북마크된 질문들을 가져옴
    bookmarked = Question.objects.filter(
        bookmark__user=request.user
    ).select_related('exam', 'category').order_by('exam__title', 'order')
    
    return render(request, 'exam/bookmarked_questions.html', {
        'questions': bookmarked
    })
    
@require_POST
@login_required
@user_is_specially_approved
def toggle_bookmark(request, question_id):
    try:
        question = get_object_or_404(Question, id=question_id)
        bookmark = Bookmark.objects.filter(
            user=request.user,  # 현재 사용자의 북마크만 조회
            question=question
        ).first()
        
        if bookmark:  # 이미 북마크가 존재하면 삭제
            bookmark.delete()
            is_bookmarked = False
        else:  # 새로 북마크 생성
            Bookmark.objects.create(
                user=request.user,
                question=question
            )
            is_bookmarked = True
            
        return JsonResponse({
            'status': 'ok',
            'is_bookmarked': is_bookmarked
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400)
        
@login_required
@user_is_specially_approved
def question_home(request):
    sections = [
        {
            "title": "Question Bank",
            "text": "ITE, 전문의 시험별 문제 은행",
            "url": reverse('exam_list'),  # Changed to always point to exam_list
            "icon_class": "fas fa-book",  # Optional: if you want to add icons
        },
        {
            "title": "Question Categories",
            "text": "단원별 문제 은행",
            "url": reverse('category_list'),
            "icon_class": "fas fa-folder",
        },
        {
            "title": "Bookmarked Questions",
            "text": "개인 북마크 문제 은행",
            "url": reverse('bookmarked_questions'),
            "icon_class": "fas fa-bookmark",
        },
    ]

    return render(request, 'exam/question_home.html', {
        'sections': sections
    })