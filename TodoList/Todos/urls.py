from django.urls import path 
from . import views

urlpatterns = [
    path('', views.display_todos),
    path('add-new-todo/', views.add_new_todo),
    path('delete_item/', views.delete_item),
    path('maps/', views.maps),
]