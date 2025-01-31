from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import SurgerySchedule
from .forms import ExcelUploadForm
from collections import defaultdict
import pandas as pd
from .models import SurgerySchedule, PatientMemo
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import ensure_csrf_cookie
import json
import logging

@login_required  # Add this decorator to ensure user is logged in
def schedule_dashboard(request):
    form = ExcelUploadForm()
    # Filter schedules by logged-in user
    schedules = SurgerySchedule.objects.filter(user=request.user).order_by("date", "room", "time_slot")

    # 방(Room)별로 데이터를 그룹화
    schedule_by_room = defaultdict(list)
    for schedule in schedules:
        schedule_by_room[schedule.room].append(schedule)

    if request.method == "POST":
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES["file"]
            df = pd.read_excel(excel_file, sheet_name="Sheet1")

            # Delete only the current user's schedules
            SurgerySchedule.objects.filter(user=request.user).delete()

            # Create new schedules associated with current user
            for index, row in df.iterrows():
                SurgerySchedule.objects.create(
                    user=request.user,  # Assign uploaded schedule to logged-in user
                    date=row["날짜"],
                    room=row["방"],
                    time_slot=row["시간"],
                    surgery_name=row["수술명"],
                    department=row["진료과"],
                    surgeon=row["집도의"],
                    duration=row["수술 시간"],
                    patient_name=row["환자명"],
                    patient_info=row["환자정보"],
                    status=row["진행 상황"]
                )

            return redirect("schedule_dashboard")

    return render(request, "schedule/dashboard.html", {
        "schedule_by_room": dict(schedule_by_room),
        "form": form
    })
    
logger = logging.getLogger(__name__)

@ensure_csrf_cookie
@require_http_methods(["GET", "POST"])
def handle_memo(request, schedule_id):
    try:
        schedule = SurgerySchedule.objects.get(id=schedule_id)
    except SurgerySchedule.DoesNotExist:
        return JsonResponse({
            'status': 'error',
            'message': 'Schedule not found'
        }, status=404)

    if request.method == "GET":
        memo = PatientMemo.objects.filter(schedule_id=schedule_id).first()
        return JsonResponse({
            'status': 'success',
            'content': memo.content if memo else ''
        })
    
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            content = data.get('content', '')
            
            memo, created = PatientMemo.objects.update_or_create(
                schedule=schedule,
                defaults={'content': content}
            )
            
            return JsonResponse({
                'status': 'success',
                'message': 'Memo saved successfully'
            })
            
        except json.JSONDecodeError:
            return JsonResponse({
                'status': 'error',
                'message': 'Invalid JSON in request body'
            }, status=400)
        except Exception as e:
            logger.error(f"Error saving memo: {str(e)}")
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=500)
