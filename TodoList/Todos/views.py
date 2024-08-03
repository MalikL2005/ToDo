from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoItem

# Create your views here.
def display_todos(req): 
    todo_list = list(ToDoItem.objects.all().values())
    print(list(todo_list))
    return render(req, 'todos.html', {'todo_list': todo_list})