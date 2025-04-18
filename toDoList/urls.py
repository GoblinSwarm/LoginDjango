from django.urls import path
from .views import create_task, login_register_view, task_view

urlpatterns = [
    path('', login_register_view, name='login'),
    path('show_tasks/', task_view, name='show-tasks'),
    path('create_task/', create_task, name='create-task'),
]