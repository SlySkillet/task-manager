from django.shortcuts import render, redirect
from .forms import TaskForm


# Create your views here.


def create_task(request):
    if request == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect("list_projects")
    else:
        form = TaskForm()

    context = {
        "form": form,
    }

    return render(request, "tasks/create.html", context)
