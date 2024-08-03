from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display_todos(req): 
    return HttpResponse("Display todos here")