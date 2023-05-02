from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
import pandas as pd
import plotly.express as px
from plotly.offline import plot

# Create your views here.


@login_required
def projects_view(request):
    projects = Project.objects.filter(owner=request.user)

    context = {"projects": projects}

    return render(request, "projects/list.html", context)


@login_required
def tasks_view(request, id):
    task = get_object_or_404(Project, id=id)

    context = {
        "tasks": task,
    }


    return render(request, "projects/detail.html", context)


@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form = form.save()
            return redirect("list_projects")
    else:
        form = ProjectForm()

    context = {
        "form": form,
    }

    return render(request, "projects/create.html", context)
