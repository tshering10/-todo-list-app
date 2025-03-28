from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .form import TaskForm
from django.contrib import messages
from .models import Task
# Create your views here.
def home(request):
    return render(request, 'taskmanager/home.html')


def dashboard(request):
    tasks = Task.objects.filter(user=request.user).order_by('completed')
    return render(request, 'taskmanager/dashboard.html',  {'tasks': tasks})
    
    
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, 'New task added successfully!')
            return redirect('dashboard')
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
            messages.success(request, 'Your task is updated successfully!')
            return redirect('dashboard')
    else:
        form = TaskForm(instance=task)
    return render(request, 'taskmanager/edit.html', {'form': form})

def delete_task(request, pk):
    task_to_delete = get_object_or_404(Task, pk=pk)
    if request.method=='POST':
        task_to_delete.delete()
        messages.success(request, 'Your task deleted successfully!')
        return redirect('dashboard')
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
                messages.info(request, 'No such tasks available.')

    context = {
        'tasks': tasks,
        'query': query,
    }
    return render(request, 'taskmanager/search.html', context)
    