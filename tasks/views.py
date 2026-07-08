from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Comment, ActivityLog
from projects.models import Project
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from notifications.models import Notification
from django.contrib import messages



@login_required
def task_list(request):

    if request.user.is_staff:

        tasks = Task.objects.all()

    else:

        tasks = Task.objects.filter(
            assigned_to=request.user
        )


    return render(
        request,
        'tasks/task_list.html',
        {
            'tasks': tasks
        }
    )



@login_required
def add_task(request):

    if request.method == "POST":


        project = request.POST.get('project')

        title = request.POST.get('title')

        description = request.POST.get('description')

        assigned_to = request.POST.get('assigned_to')

        status = request.POST.get('status')

        priority = request.POST.get('priority')

        due_date = request.POST.get('due_date')

        parent_task = request.POST.get('parent_task')



        if not project or not title or not assigned_to or not status or not priority:


            messages.error(
                request,
                "Please fill all required fields"
            )


            return redirect(
                'add_task'
            )



        assigned_user = User.objects.get(
            id=assigned_to
        )



        task = Task.objects.create(

            project_id=project,

            title=title,

            description=description,

            assigned_to=assigned_user,

            status=status,

            priority=priority,

            due_date=due_date or None,

            parent_task_id=parent_task or None

        )



        # Notification

        Notification.objects.create(

            user=assigned_user,

            message=f"You have been assigned a new task: {task.title}",

            notification_type="Assignment",

            event_key=f"assign_{task.id}"

        )



        # Activity Log

        ActivityLog.objects.create(

            task=task,

            user=request.user,

            action=f"Assigned task to {assigned_user.username}"

        )



        messages.success(
            request,
            "Task added successfully"
        )


        return redirect(
            'task_list'
        )




    projects = Project.objects.all()

    users = User.objects.all()

    tasks = Task.objects.all()



    return render(

        request,

        'tasks/add_task.html',

        {

            'projects': projects,

            'users': users,

            'tasks': tasks

        }

    )





@login_required
def edit_task(request, id):

    task = get_object_or_404(
        Task,
        id=id
    )



    if request.method == "POST":


        old_status = task.status

        new_status = request.POST['status']



        allowed_changes = {


            "Pending": [

                "In Progress"

            ],


            "In Progress": [

                "Completed"

            ],


            "Completed": []

        }



        if old_status != new_status:


            if new_status not in allowed_changes[old_status]:


                messages.error(

                    request,

                    f"Cannot change status from {old_status} to {new_status}"

                )


                return redirect(

                    'edit_task',

                    id=id

                )




        task.project_id = request.POST['project']


        task.title = request.POST['title']


        task.description = request.POST['description']


        task.assigned_to_id = request.POST['assigned_to']


        task.status = new_status


        task.priority = request.POST['priority']


        task.due_date = request.POST.get('due_date') or None


        task.parent_task_id = request.POST.get('parent_task') or None



        task.save()



        ActivityLog.objects.create(

            task=task,

            user=request.user,

            action="Updated task details"

        )



        return redirect(
            'task_list'
        )




    projects = Project.objects.all()

    users = User.objects.all()

    tasks = Task.objects.exclude(
        id=task.id
    )



    return render(

        request,

        'tasks/edit_task.html',

        {

            'task': task,

            'projects': projects,

            'users': users,

            'tasks': tasks

        }

    )





@login_required
def delete_task(request, id):

    task = get_object_or_404(
        Task,
        id=id
    )


    task.delete()


    return redirect(
        'task_list'
    )



@login_required
def task_detail(request, id):

    task = get_object_or_404(
        Task,
        id=id
    )


    comments = task.comments.all().order_by(
        "-created_at"
    )


    activities = task.activities.all().order_by(
        "-created_at"
    )



    if request.method == "POST":


        message = request.POST.get(
            "message"
        )


        if message:


            Comment.objects.create(

                task=task,

                user=request.user,

                message=message

            )


            ActivityLog.objects.create(

                task=task,

                user=request.user,

                action=f"{request.user.username} added a comment"

            )


            messages.success(
                request,
                "Comment added successfully"
            )



        return redirect(
            "task_detail",
            id=id
        )



    return render(

        request,

        "tasks/task_detail.html",

        {

            "task": task,

            "comments": comments,

            "activities": activities

        }

    )



@login_required
def delete_comment(request, id):

    comment = get_object_or_404(
        Comment,
        id=id
    )


    task = comment.task


    ActivityLog.objects.create(

        task=task,

        user=request.user,

        action=f"{request.user.username} deleted a comment"

    )


    comment.delete()


    messages.success(
        request,
        "Comment deleted successfully"
    )


    return redirect(
        "task_detail",
        id=task.id
    )




@login_required
def kanban_board(request):

    pending_tasks = Task.objects.filter(
        status='Pending'
    )


    in_progress_tasks = Task.objects.filter(
        status='In Progress'
    )


    completed_tasks = Task.objects.filter(
        status='Completed'
    )



    return render(

        request,

        'tasks/kanban.html',

        {

            'pending_tasks': pending_tasks,

            'in_progress_tasks': in_progress_tasks,

            'completed_tasks': completed_tasks

        }

    )