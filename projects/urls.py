from django.urls import path
from .views import projects_view, tasks_view, create_project, edit_project


urlpatterns = [
    path("<int:id>/edit/", edit_project, name="edit_project"),
    path("create/", create_project, name="create_project"),
    path("<int:id>/", tasks_view, name="show_project"),
    path("", projects_view, name="list_projects"),
]
