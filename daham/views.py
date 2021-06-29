from datetime import datetime

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

now = datetime.now()
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from daham.forms import BoardForm, CommentForm
from daham.models import Board, Application, Comment, Profile


def index(request):
    return render(request, 'daham/index.html')


@login_required(login_url='common:login')
def board(request):
    page = request.GET.get('page', '1')
    board_list = Board.objects.order_by('end_date')
    today = datetime.now().date()

    paginator = Paginator(board_list, 8)
    page_obj = paginator.get_page(page)

    context = {'board_list': page_obj, 'today': today}

    return render(request, 'daham/board_list.html', context)


@login_required(login_url='common:login')
def board_create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST, request.FILES)
        if form.is_valid():
            board = form.save(commit=False)  # commit=Fasle는 아직 임시저장
            board.user = request.user
            board.created_date = timezone.now()  # created_date까지 설정한 후
            board.image = form.cleaned_data['image']
            board.save()  # 진짜 저장
            return redirect('daham:board')
    else:
        form = BoardForm()
    context = {'form': form}
    return render(request, 'daham/board_form.html', context)


def detail(request, board_id):
    board = Board.objects.get(id=board_id)
    application = Application.objects.filter(board=board, user=request.user)
    context = {'board': board, 'application_list': application}

    return render(request, 'daham/board_detail.html', context)


@login_required(login_url='common:login')
def board_update(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    if request.user != board.user:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('daham:detail', board_id=board.id)

    if request.method == "POST":
        form = BoardForm(request.POST, request.FILES, instance=board)  # 기존 값을 폼에 채우기
        if form.is_valid():
            board = form.save(commit=False)
            board.user = request.user
            board.modify_date = timezone.now()
            board.image = form.cleaned_data['image']
            board.save()
            return redirect('daham:detail', board_id=board.id)
    else:
        form = BoardForm(instance=board)  # 기존 값을 폼에 채우기
    context = {'form': form}
    return render(request, 'daham/board_form.html', context)


@login_required(login_url='common:login')
def board_delete(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    if request.user != board.user:
        messages.error(request, '삭제권한이 없습니다.')
        return redirect('daham:detail', board_id=board.id)
    board.delete()
    return redirect('daham:board')


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


@login_required(login_url='common:login')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.user:
        messages.error(request, '삭제권한이 없습니다.')
        return redirect('daham:detail', board_id=comment.board.id)
    comment.delete()
    return redirect('daham:detail', board_id=comment.board.id)


def application_create(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    Application.objects.create(board=board, user=request.user, created_date=timezone.now())
    board.save()

    return redirect('daham:detail', board_id=board_id)


def application_delete(request, application_id):
    application = get_object_or_404(Application, pk=application_id)
    if request.user != application.user:
        messages.error(request, '삭제권한이 없습니다.')
        return redirect('daham:detail', board_id=application.board.id)
    application.delete()
    return redirect('daham:detail', board_id=application.board.id)


@login_required(login_url='common:login')
# 유저 프로필
def mypage(request):
    page = request.GET.get('page', '1')
    person = get_object_or_404(get_user_model(), username=request.user.username)

    application_board = Application.objects.all().filter(user=request.user)
    paginator = Paginator(application_board, 2)
    page_obj = paginator.get_page(page)

    context = {'person': person, 'board_list': page_obj}

    return render(request, 'daham/mypage.html', context)


@login_required(login_url='common:login')
def profile(request):
    if request.method == "POST":
        user_change_form = CustomUserChangeForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_change_form.is_valid() and profile_form.is_valid():
            user = user_change_form.save()
            profile_form.save()
            return redirect('people', user.username)
        return redirect('daham:profile')
    else:
        user_change_form = CustomUserChangeForm(instance=request.user)
        profile, create = Profile.objects.get_or_create(user=request.user)
        profile_form = ProfileForm(instance=profile)
        return render(request, 'daham/profile.html', {
            'user_change_form': user_change_form,
            'profile_form': profile_form
        })


#함께할래요
def want_board(request):
    page = request.GET.get('page', '1')
    board_list = Board.objects.order_by('end_date')
    today = datetime.now().date()

    paginator = Paginator(board_list, 4)
    page_obj = paginator.get_page(page)

    context = {'board_list': page_obj, 'today': today}
    return render(request, 'daham/want_board_list.html', context)


def want_board_detail(request, board_id):
    page = request.GET.get('page', '1')
    board = Board.objects.get(id=board_id)

    application_list = Application.objects.filter(board=board)
    paginator = Paginator(application_list, 5)
    page_obj = paginator.get_page(page)

    return render(request, 'daham/want_board_detail.html', {'application_list': page_obj})