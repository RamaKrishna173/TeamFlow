from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta

from projects.models import Project
from tasks.models import Task
from notifications.models import Notification


@login_required
def dashboard(request):

    total_projects = Project.objects.count()


    total_tasks = Task.objects.count()



    todo_tasks = Task.objects.filter(
        status="Pending"
    ).count()



    progress_tasks = Task.objects.filter(
        status="In Progress"
    ).count()



    completed_tasks = Task.objects.filter(
        status="Completed"
    ).count()



    overdue_tasks = Task.objects.filter(
        due_date__lt=timezone.now().date()
    ).exclude(
        status="Completed"
    ).count()



    total_notifications = Notification.objects.filter(
        user=request.user
    ).count()



    today = timezone.now().date()

    next_week = today + timedelta(days=7)



    due_tasks = Task.objects.filter(
        due_date__range=(today, next_week)
    ).order_by(
        "due_date"
    )



    # Project completion percentage

    project_task_data = []


    projects = Project.objects.all()



    for project in projects:


        total_project_tasks = Task.objects.filter(
            project=project
        ).count()



        completed_project_tasks = Task.objects.filter(
            project=project,
            status="Completed"
        ).count()



        if total_project_tasks > 0:

            completion_percentage = int(
                (completed_project_tasks / total_project_tasks) * 100
            )

        else:

            completion_percentage = 0



        project_task_data.append({

            "name": project.name,

            "percentage": completion_percentage

        })



    context = {


        "total_projects": total_projects,


        "total_tasks": total_tasks,


        "todo_tasks": todo_tasks,


        "progress_tasks": progress_tasks,


        "completed_tasks": completed_tasks,


        "overdue_tasks": overdue_tasks,


        "total_notifications": total_notifications,


        "due_tasks": due_tasks,


        "project_task_data": project_task_data,


    }



    return render(

        request,

        "dashboard/dashboard.html",

        context

    )