from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from .models import Task


# Create your views here.
def login_register_view(request):
    login_form = LoginForm(request, data=request.POST or None)
    register_form = RegisterForm(request.POST or None)

    if 'login_submit' in request.POST and login_form.is_valid():
        user = login_form.get_user()
        login(request, user)
        return redirect(reverse('show-tasks'))
    
    if 'register_submit' in request.POST and register_form.is_valid():
        user = register_form.save()
        login(request, user)
        return redirect(reverse('show-tasks'))
    
    return render(request, 'toDoList/login_register.html', {
        'login_form': login_form,
        'register_form': register_form,
        })

@login_required
def task_view(request):
    tasks = Task.objects.filter(user=request.user).order_by('-creation_date').order_by('completed')
    return render(request, 'toDoList/show_tasks.html', {'tasks': tasks})

@login_required
def create_task_view(request):
    if request.method == 'POST':
        new_task_title = request.POST.get('tarea')
        if new_task_title:
            Task.objects.create(
                user=request.user,
                title=new_task_title,
                completed=False
            )
            return redirect('show-tasks')
    return render(request, 'toDoList/create_task.html')

@login_required
def toggle_task_status_view(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    
    if request.method == 'POST':
        task.completed = not task.completed
        task.save()

    return redirect('show-tasks')
