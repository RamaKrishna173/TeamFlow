from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from projects.models import Project
from django.contrib.auth.models import User


def task_list(request):
    tasks = Task.objects.all()

    return render(request, 'tasks/task_list.html', {
        'tasks': tasks
    })


def add_task(request):

    if request.method == "POST":

        Task.objects.create(
            project_id=request.POST['project'],
            title=request.POST['title'],
            description=request.POST['description'],
            assigned_to_id=request.POST['assigned_to'],
            status=request.POST['status']
        )

        return redirect('task_list')

    projects = Project.objects.all()
    users = User.objects.all()

    return render(request, 'tasks/add_task.html', {
        'projects': projects,
        'users': users
    })


def edit_task(request, id):

    task = get_object_or_404(Task, id=id)

    if request.method == "POST":

        task.project_id = request.POST['project']
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.assigned_to_id = request.POST['assigned_to']
        task.status = request.POST['status']

        task.save()

        return redirect('task_list')


    projects = Project.objects.all()
    users = User.objects.all()

    return render(request, 'tasks/edit_task.html', {
        'task': task,
        'projects': projects,
        'users': users
    })


def delete_task(request, id):

    task = get_object_or_404(Task, id=id)

    task.delete()

    return redirect('task_list')