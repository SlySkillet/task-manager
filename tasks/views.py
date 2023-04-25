from django.shortcuts import render, redirect
from .forms import TaskForm
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def create_task(request):
    if request.method == "POST":
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
