from django.urls import path
from .views import create_task, view_tasks, project_task_chart, edit_task, delete_task


urlpatterns = [
    path("<int:id>/delete", delete_task, name="delete_task"),
    path("<int:id>/edit/", edit_task, name="edit_task"),
    path("<int:id>/", project_task_chart, name="view_chart"),
    path("mine/", view_tasks, name="show_my_tasks"),
    path("create/", create_task, name="create_task"),
]
