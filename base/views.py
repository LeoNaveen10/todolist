import django
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task
from django.views.generic import CreateView
from django.urls import reverse_lazy

class TaskList(ListView):
    model = Task
    context_object_name = 'tasks' #to give alternate name for object

class TaskDetail(DetailView):
    model = Task
    template_name = 'base/psg.html' #to give alternate name
    
class CreateTask(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')