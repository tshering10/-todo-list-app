from django.shortcuts import render, redirect, get_object_or_404
from .form import TaskForm
from django.contrib import messages
from .models import Task
# Create your views here.
def home(request):
    tasks = Task.objects.all().order_by('-pk')
    return render(request, 'taskmanager/home.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()     
    return render(request, 'taskmanager/addtask.html',{'form': form})

def edit_task(request, pk):
    #fetching the task to edit
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)
    return render(request, 'taskmanager/edit.html', {'form': form})

def delete_task(request, pk):
    task_to_delete = get_object_or_404(Task, pk=pk)
    if request.method=='POST':
        task_to_delete.delete()
        return redirect('home')
    return render(request, 'taskmanager/delete.html', {'task': task_to_delete})

def task_details(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'taskmanager/taskdetails.html', {'task':task })

def search_view(request):
    tasks = []
    query = ""

    if request.method == "POST":
        query = request.POST.get('query', '').strip()  # Get the query from POST data

        if query:
            # Search for posts with titles that match the query (case-insensitive)
            tasks = Task.objects.filter(title__icontains=query)
            if not tasks:               
                messages.warning(request, 'No such tasks available.')

    context = {
        'tasks': tasks,
        'query': query,
    }
    return render(request, 'taskmanager/search.html', context)
    