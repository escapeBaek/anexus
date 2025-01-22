from django.shortcuts import render, get_object_or_404, reverse
from .models import Exam, Question, ExamResult, Category
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from accounts.decorators import user_is_specially_approved
import json
from django.views.decorators.http import require_POST
from .models import Question,Bookmark
from urllib.parse import unquote
from django.db.models import Prefetch
from django.core.paginator import Paginator

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
    exam = get_object_or_404(Exam.objects.select_related(), pk=exam_id)
    
    # Use prefetch_related to optimize bookmark queries
    bookmarked_questions = set(Bookmark.objects.filter(
        user=request.user
    ).values_list('question_id', flat=True))
    
    # Paginate questions
    page_number = request.GET.get('page', 1)
    questions_per_page = 100  # Adjust based on your needs
    
    questions = exam.questions.all().select_related('category').order_by('order')
    paginator = Paginator(questions, questions_per_page)
    page_obj = paginator.get_page(page_number)
    
    # Add bookmark status to paginated questions
    for question in page_obj:
        question.is_bookmarked = question.id in bookmarked_questions
    
    return render(request, 'exam/question_list.html', {
        'exam': exam,
        'questions': page_obj,
        'page_obj': page_obj,
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
        
        # detailed_results에 question_id 추가
        for detail in detailed_results:
            try:
                question = Question.objects.filter(text=detail['question']).first()
                if question:
                    detail['question_id'] = question.id
            except Exception:
                continue

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

    # Get bookmarked questions
    bookmarked_questions = set(
        Bookmark.objects.filter(user=request.user).values_list('question_id', flat=True)
    )

    # Create a lookup dictionary using values() to get dictionary objects
    questions_lookup = {
        str(q['question_text'])[:50]: q['id']  # Convert to string to ensure consistency
        for q in Question.objects.values('id', 'question_text')
    }

    # Process the detailed results
    updated_results = []
    for detail in result.detailed_results:
        question_text = str(detail.get('question', ''))[:50]  # Convert to string and limit length
        question_id = questions_lookup.get(question_text)
        
        updated_detail = detail.copy()
        updated_detail['question_id'] = question_id
        updated_detail['is_bookmarked'] = question_id in bookmarked_questions if question_id else False
        updated_results.append(updated_detail)

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
    # URL 디코딩된 카테고리 이름으로 검색
    decoded_category_name = unquote(category_name)
    try:
        category = get_object_or_404(Category, name=decoded_category_name)
        questions = Question.objects.filter(category=category).order_by('order')
        return render(request, 'exam/category_questions.html', {
            'category_name': category.name,
            'questions': questions
        })
    except Category.DoesNotExist:
        # 카테고리를 찾을 수 없을 때 로깅 추가
        print(f"Category not found: {decoded_category_name}")
        raise Http404(f"Category not found: {decoded_category_name}")
    
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