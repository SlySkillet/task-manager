from django.urls import path
from .views import projects_view, tasks_view, create_project


urlpatterns = [
    path("create/", create_project, name="create_project"),
    path("<int:id>/", tasks_view, name="show_project"),
    path("", projects_view, name="list_projects"),
]
