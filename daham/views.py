from django.shortcuts import render

from daham.models import Board


def index(request):
    board_list = Board.objects.order_by('-created_date')
    context = {'board_list': board_list}

    return render(request, 'daham/board_list.html', context)

def detail(request, board_id):
    board = Board.objects.get(id=board_id)
    context = {'board': board}

    return render(request, 'daham/board_detail.html', context)