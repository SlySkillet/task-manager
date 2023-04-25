from django.urls import path
from .views import projects_view, tasks_view


urlpatterns = [
    path("<int:id>/", tasks_view, name="show_project"),
    path("", projects_view, name="list_projects")
]
