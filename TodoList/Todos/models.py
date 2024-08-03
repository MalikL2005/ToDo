from django.db import models

# Create your models here.
class ToDoItem(models.Model):
    title = models.CharField(max_length=100, default="New ToDo-Item")
    description = models.CharField(max_length=500)
    address = models.CharField(max_length=500, null=True)
    checked = models.BooleanField(default=False)
