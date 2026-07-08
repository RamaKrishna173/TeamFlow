from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.task_list,
        name='task_list'
    ),


    path(
        'add/',
        views.add_task,
        name='add_task'
    ),


    path(
        'edit/<int:id>/',
        views.edit_task,
        name='edit_task'
    ),


    path(
        'delete/<int:id>/',
        views.delete_task,
        name='delete_task'
    ),


    path(
        'detail/<int:id>/',
        views.task_detail,
        name='task_detail'
    ),


    path(
        'kanban/',
        views.kanban_board,
        name='kanban_board'
    ),
    path(
     'comment/delete/<int:id>/',
     views.delete_comment,
     name='delete_comment'
     ),

]