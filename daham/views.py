from django.shortcuts import render, redirect
from django.utils import timezone

from daham.models import Board


def index(request):
    board_list = Board.objects.order_by('-created_date')
    context = {'board_list': board_list}

    return render(request, 'daham/board_list.html', context)
    # return render(request, 'daham/board_list.html')


def detail(request, board_id):
    board = Board.objects.get(id=board_id)
    context = {'board': board}

    return render(request, 'daham/board_detail.html', context)


def comment_create(request, board_id):
    board = Board.objects.get(id=board_id)
    if request.POST.get('content') != '':
        board.comment_set.create(content=request.POST.get('content'), created_date=timezone.now())

    return redirect('daham:detail', board_id=board.id)
