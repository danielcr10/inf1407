from django.contrib.auth.models import Group
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import TaskForm
from django.contrib import messages
from django.http import HttpResponseForbidden

from .models import Tarefa

@login_required
def taskList(request):
    search = request.GET.get('search')
    if search:
        l = []
        for g in request.user.groups.all():
            l.append(g.name)
        tasks = Tarefa.objects.filter(titulo__icontains=search, setor__in=l)
    else:
        l = []
        for g in request.user.groups.all():
            l.append(g.name)
        # tasks_list = Tarefa.objects.all().order_by('created_at').filter(user=request.user)
        tasks_list = Tarefa.objects.all().order_by('created_at').filter(setor__in=l)
        paginator = Paginator(tasks_list, 10)
        page = request.GET.get('page')
        tasks = paginator.get_page(page)
    return render(request, 'tasks/list.html', {'tasks':tasks})

@login_required
def mytaskList(request):
    search = request.GET.get('search')
    if search:
        tasks = Tarefa.objects.filter(titulo__icontains=search, user=request.user)
    else:
        l = []
        for g in request.user.groups.all():
            l.append(g.name)
        # tasks_list = Tarefa.objects.all().order_by('created_at').filter(user=request.user)
        tasks_list = Tarefa.objects.all().order_by('created_at').filter(user=request.user)
        paginator = Paginator(tasks_list, 10)
        page = request.GET.get('page')
        tasks = paginator.get_page(page)
    return render(request, 'tasks/mylist.html', {'tasks':tasks})

@login_required
def taskView(request, id):
    task = get_object_or_404(Tarefa, pk=id)
    return render(request, 'tasks/task.html', {'task': task})

@login_required
def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        
        if form.is_valid():
            task = form.save(commit=False)
            task.situacao = 'doing'
            task.user = request.user
            task.save()
            return redirect('/')
    else:
        form = TaskForm()
        return render(request, 'tasks/addtask.html', {'form': form})

@login_required
def editTask(request, id):
    task = get_object_or_404(Tarefa, pk=id)
    if task.user != request.user:
        return HttpResponseForbidden()
    form = TaskForm(instance=task)

    if(request.method == 'POST'):
        form = TaskForm(request.POST, instance=task)

        if(form.is_valid()):
            task.save()
            return redirect('/')
        else:
            return render(request, 'task/edittask.html', {'form': form, 'task': task})
    else:
        return render(request, 'tasks/edittask.html', {'form': form, 'task': task})

@login_required
def deleteTask(request, id):
    task = get_object_or_404(Tarefa, pk=id)
    if task.user != request.user:
        return HttpResponseForbidden()
    task.delete()

    messages.info(request, 'Tarefa deletada com sucesso.')

    return redirect('/')

def helloWorld(request):
    return HttpResponse('Hello world!')