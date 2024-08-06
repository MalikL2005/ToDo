from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import HttpResponsePermanentRedirect
from Todos.models import ToDoItem
from django.contrib import messages
import os
# Create your views here.

def start_nav(req): 
    try: 
        items = ToDoItem.objects.all().values_list()
        item=items[0]
        print(item)
    except: 
        #pop up alert (No todos)
        print("No Todos Here")
        
        return HttpResponsePermanentRedirect(os.environ['URL'])
    return HttpResponsePermanentRedirect(f'items/{item[4]}')

def navigate(req, pk):
    try: 
        item = ToDoItem.objects.get(id=pk) 
        start= ''
        destination = ''
        maps_url = f'https://www.google.com/maps/dir/{start}/{destination}'
        # print(maps_url)
        context = {'item': item, 'maps_url': maps_url}
    except:
        return HttpResponsePermanentRedirect(os.environ['URL'])
    return render(req, 'nav_base.html', context)

def remove_todo_item(req, pk):
    item_to_delete = ToDoItem.objects.filter(pk=pk).delete()
    print(item_to_delete)
    return HttpResponsePermanentRedirect(os.environ['URL']+'nav')
   