from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import TaskForm

from .models import Tarefa

def taskList(request):
    tasks = Tarefa.objects.all().order_by('created_at')
    return render(request, 'tasks/list.html', {'tasks':tasks})

def taskView(request, id):
    task = get_object_or_404(Tarefa, pk=id)
    return render(request, 'tasks/task.html', {'task': task})

def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        
        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.save()
            return redirect('/')
    else:
        form = TaskForm()
        return render(request, 'tasks/addtask.html', {'form': form})

def helloWorld(request):
    return HttpResponse('Hello world!')