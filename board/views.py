from django.shortcuts import render, get_object_or_404, redirect
from board.models import Board
from .forms import BoardForm
from django.contrib.auth.decorators import login_required

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

@login_required
def board_create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.author = request.user
            board.save()
            return redirect('board_index')
    else:
        form = BoardForm()
    return render(request, 'board/board_form.html', {'form': form})
