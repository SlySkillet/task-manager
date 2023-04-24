from django.shortcuts import render
from .models import Project

# Create your views here.


def projects_view(request):
    projects = Project.objects.all()

    context = {
        "projects": projects
    }

    return render(request, "projects/list.html", context)
