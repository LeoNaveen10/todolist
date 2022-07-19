from asyncio import tasks
from weakref import ReferenceType
import django
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

class CustomLogin(LoginView):
    fields = '__all__'
    template_name = 'base/login.html'
    redirect_authenticated_user: True
    
    def get_success_url(self) -> str:
        return reverse_lazy('tasks')
    

class TaskList(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = 'tasks' #to give alternate name for object

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user = self.request.user)
        context['count'] = context['tasks'].filter(complete = False).count()
        return context
    
class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    template_name = 'base/psg.html' #to give alternate name
    
class CreateTask(LoginRequiredMixin,CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    
class UpdateTask(LoginRequiredMixin,UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    
class DeleteTask(LoginRequiredMixin,DeleteView):
    model= Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')