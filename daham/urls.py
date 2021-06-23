from django.urls import path

from . import views

app_name = 'daham'

urlpatterns = [
    path('', views.index, name='index'),
    path('board/', views.board, name='board'),
    path('board/<int:board_id>/', views.detail, name='detail'),
    path('board/create', views.board_create, name='board_create'),
    path('board/update/<int:board_id>/', views.board_update, name='board_update'),
    path('board/delete/<int:board_id>/', views.board_delete, name='board_delete'),
    path('board/<int:board_id>/comment/create/', views.comment_create, name='comment_create'),
    path('board/<int:board_id>/application/create', views.application_create, name='application_create'),
    path('comment/update/<int:comment_id>/', views.comment_update, name='comment_update'),
    path('comment/delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),
]