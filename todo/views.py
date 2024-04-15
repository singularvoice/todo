from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import TodoItem


def todo_list(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo_list.html', {'todos': todos})


def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        TodoItem.objects.create(title=title)
        return redirect('todo_list')
    return render(request, 'add_todo.html')


def delete_todo(request, todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    todo.delete()
    return redirect('todo_list')


def toggle_todo(request,todo_id):
    if request.method == 'POST':
        todo = get_object_or_404(TodoItem, pk=todo_id)
        todo.completed = not todo.completed  # Toggle completed status
        todo.save()
        return HttpResponseRedirect(reverse('todo_list'))
    return HttpResponseRedirect(reverse('todo_list'))
