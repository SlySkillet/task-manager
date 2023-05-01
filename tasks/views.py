from django.shortcuts import render, redirect
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
    tasks = Task.objects.filter(assignee=request.user)

    qs = Task.objects.filter(assignee=request.user)
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
        "tasks": tasks,
        'plot_div': gantt_plot,
    }

    return render(request, 'tasks/list.html', context)
