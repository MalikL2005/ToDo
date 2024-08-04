from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect

# Create your views here.
def get_map(req):
    
    address = ""
    return HttpResponsePermanentRedirect('https://www.google.com/maps/place/'+ address)