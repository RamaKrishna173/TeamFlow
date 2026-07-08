from django.shortcuts import render, redirect, get_object_or_404
from .models import Project
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from tasks.models import Task

@login_required
@login_required
def project_list(request):

    projects = Project.objects.all()

    project_data = []

    for project in projects:

        total_tasks = Task.objects.filter(
            project=project
        ).count()

        completed_tasks = Task.objects.filter(
            project=project,
            status="Completed"
        ).count()

        if total_tasks > 0:

            progress = int(
                (completed_tasks / total_tasks) * 100
            )

        else:

            progress = 0

        project_data.append({

            "project": project,

            "total_tasks": total_tasks,

            "completed_tasks": completed_tasks,

            "progress": progress,

        })

    return render(

        request,

        "projects/project_list.html",

        {

            "project_data": project_data

        }

    )


@login_required
def add_project(request):

    if request.method == "POST":


        name = request.POST.get('name')

        description = request.POST.get('description')

        start_date = request.POST.get('start_date')

        end_date = request.POST.get('end_date')

        priority = request.POST.get('priority')

        status = request.POST.get('status')



        if not name or not description or not start_date or not end_date or not priority or not status:


            messages.error(
                request,
                "Please fill all entries"
            )


            return redirect('add_project')



        Project.objects.create(

            name=name,

            description=description,

            start_date=start_date,

            end_date=end_date,

            priority=priority,

            status=status

        )



        messages.success(
            request,
            "Project added successfully"
        )


        return redirect('project_list')



    return render(
        request,
        'projects/add_project.html'
    )





@login_required
def edit_project(request, id):

    project = get_object_or_404(
        Project,
        id=id
    )


    if request.method == "POST":


        name = request.POST.get('name')

        description = request.POST.get('description')

        start_date = request.POST.get('start_date')

        end_date = request.POST.get('end_date')

        priority = request.POST.get('priority')

        status = request.POST.get('status')



        if not name or not description or not start_date or not end_date or not priority or not status:


            messages.error(
                request,
                "Please fill all entries"
            )


            return redirect(
                'edit_project',
                id=id
            )



        project.name = name

        project.description = description

        project.start_date = start_date

        project.end_date = end_date

        project.priority = priority

        project.status = status


        project.save()



        messages.success(
            request,
            "Project updated successfully"
        )


        return redirect('project_list')



    return render(
        request,
        'projects/edit_project.html',
        {
            'project': project
        }
    )





@login_required
def delete_project(request, id):

    project = get_object_or_404(
        Project,
        id=id
    )


    project.delete()


    messages.success(
        request,
        "Project deleted successfully"
    )


    return redirect('project_list')