from django.shortcuts import render
from .models import ToDoItem
from django.http import HttpResponsePermanentRedirect
from django.http import HttpResponse

# Create your views here.
def display_todos(req):
    todo_list = list(ToDoItem.objects.all().values())
    return render(req, 'base.html', {'todo_list': todo_list})

def add_new_todo(req):
    if req.method == 'POST': 
        try: new_item = ToDoItem.objects.create(title=req.POST['title'], description=req.POST['description'], address=req.POST['address'])
        except: print("Could not add item to db")
    return HttpResponsePermanentRedirect('http://localhost:8000/todos/')

def delete_item(req):
    if req.method == 'POST':
        id = req.POST['delete_item']
        item = ToDoItem.objects.filter(id=id).delete()
    return HttpResponsePermanentRedirect('http://localhost:8000/todos/')

def maps(req):
    address = req.GET['show_map']
    print(address)
    return HttpResponsePermanentRedirect(f'https://www.google.com/maps/place/{address}/')
