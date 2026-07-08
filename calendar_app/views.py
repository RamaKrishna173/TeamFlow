from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST

from tasks.models import Task
from projects.models import Project

import json




@login_required
def calendar(request):


    context = {


        "projects": Project.objects.all(),


        "users": User.objects.all(),


    }



    return render(

        request,

        "calendar/calendar.html",

        context

    )







@login_required
def events(request):


    tasks = Task.objects.select_related(

        "project",

        "assigned_to"

    )




    project = request.GET.get("project")

    status = request.GET.get("status")

    priority = request.GET.get("priority")

    assigned = request.GET.get("assigned")





    if project:


        tasks = tasks.filter(

            project_id=project

        )




    if status:


        tasks = tasks.filter(

            status=status

        )




    if priority:


        tasks = tasks.filter(

            priority=priority

        )




    if assigned:


        tasks = tasks.filter(

            assigned_to_id=assigned

        )






    events = []





    for task in tasks:



        if not task.due_date:

            continue





        if task.priority == "High":

            color = "#ef4444"


        elif task.priority == "Medium":

            color = "#f59e0b"


        elif task.priority == "Low":

            color = "#22c55e"


        else:

            color = "#3b82f6"







        events.append({


            "id": task.id,


            "title": task.title,


            "start": str(task.due_date),



            "backgroundColor": color,


            "borderColor": color,


            "textColor": "#ffffff",





            "extendedProps": {



                "project": task.project.name,



                "status": task.status,



                "priority": task.priority,



                "assigned": (

                    task.assigned_to.username

                    if task.assigned_to

                    else "Not Assigned"

                ),



                "description": task.description,


            }


        })





    return JsonResponse(

        events,

        safe=False

    )








@require_POST
@login_required
def update_event(request):


    data = json.loads(

        request.body

    )



    task = get_object_or_404(

        Task,

        id=data["id"]

    )



    task.due_date = data["start"]


    task.save()



    return JsonResponse({


        "success": True


    })