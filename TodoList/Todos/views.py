from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoItem
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def display_todos(req):
    if req.method == 'POST': 
        try: new_item = ToDoItem.objects.create(title=req.POST['title'], description=req.POST['description'], address=req.POST['address'])
        except: print("Could not add item to db")
    todo_list = list(ToDoItem.objects.all().values())
    return render(req, 'todos.html', {'todo_list': todo_list})


