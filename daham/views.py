from datetime import datetime

from django.contrib.auth.decorators import login_required

now = datetime.now()
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from daham.forms import BoardForm, CommentForm
from daham.models import Board, Application


def index(request):
    return render(request, 'daham/index.html')


def board(request):
    page = request.GET.get('page', '1')
    board_list = Board.objects.order_by('end_date')
    today = datetime.now().date()

    paginator = Paginator(board_list, 4)
    page_obj = paginator.get_page(page)

    context = {'board_list': page_obj, 'today': today}

    return render(request, 'daham/board_list.html', context)


@login_required(login_url='common:login')
def board_create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)  # commit=Fasle는 아직 임시저장
            board.user = request.user
            board.created_date = timezone.now()  # created_date까지 설정한 후
            board.save()  # 진짜 저장
            return redirect('daham:board')
    else:
        form = BoardForm()
    context = {'form': form}
    return render(request, 'daham/board_form.html', context)


def detail(request, board_id):
    board = Board.objects.get(id=board_id)
    context = {'board': board}

    return render(request, 'daham/board_detail.html', context)


@login_required(login_url='common:login')
def comment_create(request, board_id):
    board = get_object_or_404(Board, pk=board_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.board = board
            comment.save()
            return redirect('daham:detail', board_id=board.id)
    else:
        form = CommentForm()
    context = {'board': board, 'form': form}
    return render(request, 'daham/board_detail.html', context)


def application_create(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    Application.objects.create(board=board, user=request.user, created_date=timezone.now())
    board.save()

    return redirect('daham:board')

