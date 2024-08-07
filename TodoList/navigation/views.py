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
        print(item.address)
        if item.address:
            destination = item.address.replace(' ', '+')
        start= 'Poppelsdorfer+Schloss,+Meckenheimer+Allee+171,+53115+Bonn'.replace(' ', '+')
        API_KEY = os.environ['API_KEY_TWO']
        # maps_url = f'https://www.google.com/maps/dir/Hobsweg+64,+53125+Bonn,+Deutschland/Am+Alten+Stauwehr+1,+53340+Meckenheim,+Deutschland/@50.6682948,6.965657,12z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x47bee25a746bb87f:0xbb419df7fd43f7ef!2m2!1d7.0755759!2d50.6794474!1m5!1m1!1s0x47bf1d549bf1f6bd:0x2e9f5e644fb89c87!2m2!1d7.0195342!2d50.6360963!3e0?hl=de-DE&entry=ttu'
        # maps_url = f'https://www.google.com/maps/dir/?key={API_KEY}&origin={start}&destination={destination}'
        maps_url = f'https://www.google.com/maps/embed/v1/place?key={API_KEY}&q={destination}'
        print(maps_url)
        context = {'item': item, 'maps_url': maps_url}
    except:
        return HttpResponsePermanentRedirect(os.environ['URL'])
    return render(req, 'nav_base.html', context)

def remove_todo_item(req, pk):
    item_to_delete = ToDoItem.objects.filter(pk=pk).delete()
    print(item_to_delete)
    return HttpResponsePermanentRedirect(os.environ['URL']+'nav')
   