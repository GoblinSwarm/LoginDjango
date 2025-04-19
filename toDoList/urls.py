from django.urls import path
from django.contrib.auth import views as auth_views
from .views import create_task_view, login_register_view, task_view, toggle_task_status_view

urlpatterns = [
    path('', login_register_view, name='login'),
    path('show_tasks/', task_view, name='show-tasks'),
    path('create_task/', create_task_view, name='create-task'),
    path('toggle_task/<int:task_id>/', toggle_task_status_view, name='toggle-task'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]