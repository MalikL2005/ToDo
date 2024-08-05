from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponsePermanentRedirect
from Todos.models import ToDoItem
import os
# Create your views here.

def start_nav(req): 
    items = ToDoItem.objects.all().values_list()
    item=items[0]
    return HttpResponseRedirect(f'items/{item[4]}')

def navigate(req, pk):
    item = ToDoItem.objects.get(id=pk)
    url = os.environ['URL']
    start= ''
    destination = ''
    maps_url = f'https://www.google.com/maps/dir/{start}/{destination}'
    print(maps_url)
    context = {'url': f'{url}nav/', 'item': item, 'maps_url': maps_url}
    return render(req, 'nav_base.html', context)