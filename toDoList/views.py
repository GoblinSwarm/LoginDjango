from django.shortcuts import render, redirect, reverse
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
        #En este caso hay que modificarlo para que redirija a la vista de tareas
        return redirect('home')
    
    if 'register_submit' in request.POST and register_form.is_valid():
        user = register_form.save(commit=False)
        user.set_password(register_form.cleaned_data['password'])
        user.save()
        #Aca se puede hacer un logueo directo 
        return redirect('login')
    
    return render(request, 'toDoList/login_register.html', {
        'login_form': login_form,
        'register_form': register_form,
        })

def task_view(request):
    tasks = Task.objects.all()
    return render(request, 'toDoList/show_tasks.html', {'tasks': tasks})


def create_task(request):
    if request.POST:
        new_task = request.POST.get('tarea')
        Task.objects.create(description=new_task, done=False)
        return redirect(reverse('create-task'))
    return render(request, 'toDoList/create_task.html')
