from django.shortcuts import render, redirect, get_object_or_404
from board.models import Board
from board.forms import BoardForm

# 글 목록
def board_index(request):
    boards = Board.objects.all()
    context = {
        'boards': boards
    }
    return render(request, 'board/board_index.html', context)

# 글 상세보기
def board_detail(request, pk):
    board = get_object_or_404(Board, pk=pk)
    context = {
        'board': board
    }
    return render(request, 'board/board_detail.html', context)

# 글 작성
def board_create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('board_index')
    else:
        form = BoardForm()
    return render(request, 'board/board_form.html', {'form': form})
