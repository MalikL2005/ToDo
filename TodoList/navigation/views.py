from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import HttpResponsePermanentRedirect
from Todos.models import ToDoItem
import os
# Create your views here.

def start_nav(req): 
    print("Starting")
    try: 
        items = ToDoItem.objects.all().values_list()
        item=items[0]
    except:
        return HttpResponsePermanentRedirect(os.environ['URL'])
    print(item)
    return HttpResponseRedirect(f'items/{item[4]}')

def navigate(req, pk):
    item = ToDoItem.objects.get(id=pk) 
    start= ''
    destination = ''
    maps_url = f'https://www.google.com/maps/dir/{start}/{destination}'
    print(maps_url)
    context = {'item': item, 'maps_url': maps_url}
    return render(req, 'nav_base.html', context)

def remove_todo_item(req, pk):
    item_to_delete = ToDoItem.objects.filter(id=pk).delete()
    print(item_to_delete)
    return HttpResponsePermanentRedirect(os.environ['URL']+'/nav')

