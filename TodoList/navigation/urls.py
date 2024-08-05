from django.urls import path 
from . import views 

urlpatterns=[
    path('', views.start_nav),
    path('items/<int:pk>', views.navigate),
]