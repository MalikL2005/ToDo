from django.shortcuts import render
from .models import ToDoItem
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponsePermanentRedirect

# Create your views here.
@csrf_exempt
def display_todos(req):
    todo_list = list(ToDoItem.objects.all().values())
    return render(req, 'todos.html', {'todo_list': todo_list})

def add_new_todo(req):
    if req.method == 'POST': 
        try: new_item = ToDoItem.objects.create(title=req.POST['title'], description=req.POST['description'], address=req.POST['address'])
        except: print("Could not add item to db")
    return HttpResponsePermanentRedirect('http://localhost:8000/todos/')

