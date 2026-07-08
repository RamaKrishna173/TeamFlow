import csv
from django.http import HttpResponse
from projects.models import Project
from tasks.models import Task
from django.shortcuts import render

def reports_home(request):
    return render(request, "reports/index.html")


def export_projects(request):

    response = HttpResponse(
        content_type='text/csv'
    )

    response['Content-Disposition'] = 'attachment; filename="projects.csv"'

    writer = csv.writer(response)

    writer.writerow([
        'Name',
        'Status',
        'Start Date',
        'End Date'
    ])

    projects = Project.objects.all()

    for project in projects:
        writer.writerow([
            project.name,
            project.status,
            project.start_date,
            project.end_date
        ])

    return response



def export_tasks(request):

    response = HttpResponse(
        content_type='text/csv'
    )

    response['Content-Disposition'] = 'attachment; filename="tasks.csv"'

    writer = csv.writer(response)

    writer.writerow([
        'Title',
        'Project',
        'Assigned User',
        'Status'
    ])

    tasks = Task.objects.all()

    for task in tasks:
        writer.writerow([
            task.title,
            task.project.name,
            task.assigned_to.username if task.assigned_to else '',
            task.status
        ])

    return response