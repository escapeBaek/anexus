from django.shortcuts import render, get_object_or_404
from board.models import Board

# Create your views here.

def board_index(request):
    boards = Board.objects.all()
    context = {
        'boards': boards
    }
    return render(request, 'board/board_index.html', context)

def board_detail(request, pk):
    board = get_object_or_404(Board, pk=pk)
    context = {
        'board': board
    }
    return render(request, 'board/board_detail.html', context)
