from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem


def home(request):
    todos = TodoItem.objects.all()
    return render(request, 'index.html', {'todos': todos})


def remaining(request):
    todos = TodoItem.objects.all().filter(completed=False)
    return render(request, 'remaining.html', {'todos': todos})


def completed(request):
    todos = TodoItem.objects.all().filter(completed=True)
    return render(request, 'completed.html', {'todos': todos})


def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        due_time = request.POST.get('due_time')

        if title != "":
            todo = TodoItem(title=title, description=description, due_date=due_date, due_time=due_time, completed=False)
            todo.save()
            return redirect('home')
    return render(request, 'add_todo.html')


def request_to_delete_todo(request,todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    return render(request, 'delete_todo.html',{'todo':todo})


def todo_detail(request, todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    return render(request, 'todo_detail.html', {'todo': todo})


def toggle_todo(request, todo_id):
    todo = get_object_or_404(TodoItem, id=todo_id)
    todo.completed = not todo.completed  # Toggle completed status
    todo.save()
    return redirect(request.META.get('HTTP_REFERER'))


def delete_todo(request, todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    todo.delete()
    return redirect('home')


