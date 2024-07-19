from django.shortcuts import get_object_or_404, render, redirect
from .models import Task
from .forms import CreateTasksForm, EditTasksForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def tasksView(request):
    owner = request.user
    tasks = Task.objects.filter(owner=owner)
    
    context = {
        'tasks': tasks
    }
    return render(request, 'tasks/tasks.html', context)

@login_required
def createTaskView(request):
    form = CreateTasksForm(request.POST or None)
    
    context = {
        'form': form
    }
    
    if form.is_valid():
        new_task = form.save(commit=False)
        new_task.owner = request.user
        new_task.save()
        return redirect('tasks:tasks')
    
    return render(request, 'tasks/createTask.html', context)

@login_required
def editTaskView(request, id):
    task = get_object_or_404(Task, pk=id)
    
    if request.method == 'GET':
        form = EditTasksForm(instance=task)
        return render(request, 'tasks/editTask.html', {'form': form})
        
    else:
        form = EditTasksForm(request.POST, instance=task)
        form.save()
        return redirect('tasks:tasks')
    
    

@login_required
def deleteTaskView(request, id):
    
    task = get_object_or_404(Task, pk=id)
    task.delete()
    return redirect('tasks:tasks')

