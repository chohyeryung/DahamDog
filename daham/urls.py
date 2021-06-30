from django.conf.urls.static import static
from django.urls import path

from config import settings
from . import views

app_name = 'daham'

urlpatterns = [
    path('', views.index, name='index'),
    path('intro/', views.intro, name='intro'),
    path('board/', views.board, name='board'),
    path('board/<int:board_id>/', views.detail, name='detail'),
    path('board/create/', views.board_create, name='board_create'),
    path('board/update/<int:board_id>/', views.board_update, name='board_update'),
    path('board/delete/<int:board_id>/', views.board_delete, name='board_delete'),
    path('board/<int:board_id>/comment/create/', views.comment_create, name='comment_create'),
    path('board/<int:board_id>/application/create/', views.application_create, name='application_create'),
    path('application/delete/<int:application_id>/', views.application_delete, name='application_delete'),
    path('comment/delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    path('mypage/', views.mypage, name='mypage'),
    path('profile/', views.profile, name='profile'),
    # 함께할래요
    path('want_board/', views.want_board, name='want_board'),
    path('want_board/<int:board_id>/', views.want_board_detail, name='want_board_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
