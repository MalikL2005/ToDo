from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponsePermanentRedirect
from Todos.models import ToDoItem
import os
# Create your views here.

def start_nav(req): 
    items = ToDoItem.objects.all().values_list()
    print(items)
    item=items[0]
    return HttpResponseRedirect(f'items/{item[4]}')

def navigate(req, pk):
    item = ToDoItem.objects.get(id=pk)
    url = os.environ['URL']
    context = {'url': f'{url}nav/', 'item': item}
    return render(req, 'nav_base.html', context)