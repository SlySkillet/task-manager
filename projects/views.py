from django.shortcuts import render, get_object_or_404
from .models import Project
from tasks.models import Task
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def projects_view(request):
    projects = Project.objects.filter(owner=request.user)

    context = {
        "projects": projects
    }

    return render(request, "projects/list.html", context)


@login_required
def tasks_view(request, id):
    tasks = get_object_or_404(Task, id=id)

    context = {
        "tasks": tasks,
    }

    return render(request, "projects/detail.html", context)
