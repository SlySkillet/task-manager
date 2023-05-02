from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import Task
from django.contrib.auth.decorators import login_required
import pandas as pd
import plotly.express as px
from plotly.offline import plot

# Create your views here.


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form = form.save()
            return redirect("list_projects")
    else:
        form = TaskForm()

    context = {
        "form": form,
    }

    return render(request, "tasks/create.html", context)


# @login_required
# def view_tasks(request):
#     tasks = Task.objects.filter(assignee=request.user)

#     context = {
#         "tasks": tasks,
#     }

#     return render(request, "tasks/list.html", context)

# --GANTT CHART EXPERIMENT--
@login_required
def view_tasks(request):
    qs = Task.objects.filter(assignee=request.user)
    if request.method == "POST":
        id_list = request.POST.getlist("boxes")
        for x in id_list:
            Task.objects.filter(pk=int(x)).update(is_complete=True)
        return(redirect("show_my_tasks"))
    projects_data = [
        {
            'Project': task.name,
            'Start': task.start_date,
            'Finish': task.due_date,
            'Responsible': task.assignee,
        } for task in qs
    ]
    df = pd.DataFrame(projects_data)
    fig = px.timeline(
        df, x_start="Start", x_end="Finish", y="Project", color="Responsible"
    )
    fig.update_yaxes(autorange="reversed")
    gantt_plot = plot(fig, output_type="div")

    context = {
        "tasks": qs,
        'plot_div': gantt_plot,
    }

    return render(request, 'tasks/list.html', context)


@login_required
def edit_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("show_my_tasks")
    else:
        form = TaskForm(instance=task)

    context = {
        "task": task,
        "form": form,
    }

    return render(request, "tasks/edit.html", context)


@login_required
def project_task_chart(request, id):

    qs = Task.objects.filter(project=id)
    projects_data = [
        {
            'Project': task.name,
            'Start': task.start_date,
            'Finish': task.due_date,
            'Responsible': task.assignee,
        } for task in qs
    ]
    df = pd.DataFrame(projects_data)
    fig = px.timeline(
        df, x_start="Start", x_end="Finish", y="Project", color="Responsible"
    )
    fig.update_yaxes(autorange="reversed")
    gantt_plot = plot(fig, output_type="div")

    context = {
        "plot_div": gantt_plot,
        "tasks": qs,
    }

    return render(request, 'tasks/chart.html', context)
