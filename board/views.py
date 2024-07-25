from django.shortcuts import render
from board.models import Board
# Create your views here.

def board_index(request):
    boards = Board.objects.all()
    context = {
        'boards': boards
    }
    return render(request, 'board/board_index.html', context)

# aneshub/board/views.py:
def board_detail(request, pk):
    board = Board.objects.get(pk=pk)
    context = {
        'board': board
    }
    return render(request, 'board/board_detail.html', context)