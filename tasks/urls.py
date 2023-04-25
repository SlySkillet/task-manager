from django.urls import path
from .views import create_task, view_tasks


urlpatterns = [
    path("mine/", view_tasks, name="show_my_tasks"),
    path("create/", create_task, name="create_task"),
]
