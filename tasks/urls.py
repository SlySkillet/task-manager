from django.urls import path
from .views import create_task, view_tasks, project_task_chart


urlpatterns = [
    path("<int:id>/", project_task_chart, name="view_chart"),
    path("mine/", view_tasks, name="show_my_tasks"),
    path("create/", create_task, name="create_task"),
]
