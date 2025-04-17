from django.urls import path
from .views import create_task, login_register_view

urlpatterns = [
    path('', login_register_view, name='login'),
    path('create_task/', create_task, name='create-task'),
]