# board/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Board
from .forms import BoardForm


def board_index(request):
    boards = Board.objects.all()
    return render(request, 'board/board_index.html', {'boards': boards})

@login_required
def board_detail(request, pk):
    board = get_object_or_404(Board, pk=pk)
    context = {
        'board': board,
        'can_edit': request.user == board.author  # 현재 사용자가 작성자인지 확인
    }
    return render(request, 'board/board_detail.html', context)

@login_required
def board_edit(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.user != board.author:
        # 권한이 없는 사용자가 접근하려 할 때
        return redirect('board_detail', pk=pk)

    if request.method == 'POST':
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            form.save()
            return redirect('board_detail', pk=pk)
    else:
        form = BoardForm(instance=board)
    
    return render(request, 'board/board_form.html', {'form': form})

@login_required
def board_delete(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.user != board.author:
        return redirect('board_detail', pk=pk)

    if request.method == 'POST':
        board.delete()
        return redirect('board_index')

    return render(request, 'board/board_confirm_delete.html', {'board': board})

def board_create(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.author = request.user  # 현재 로그인한 사용자로 설정
            board.save()
            return redirect('board_index')
    else:
        form = BoardForm()
    return render(request, 'board/board_form.html', {'form': form})