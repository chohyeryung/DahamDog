from django.urls import path

from . import views

app_name = 'daham'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:board_id>/', views.detail, name='detail'),
    path('board/create', views.board_create, name='board_create'),
    path('board/<int:board_id>/comment/create/', views.comment_create, name='comment_create'),
    path('board/<int:board_id>/application/create', views.application_create, name='application_create'),
]