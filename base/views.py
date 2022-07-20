
import django
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class CustomLogin(LoginView):
    fields = '__all__'
    template_name = 'base/login.html'
    redirect_authenticated_user= True
    
    def get_success_url(self):
        return reverse_lazy('tasks')
    
class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')    

    def form_valid(self, form):
        user = form.save()  #save the user
        if user is not None: 
            login(self.request,user) #login method is called
        return super(RegisterPage,self).form_valid(form) 
    
    #authenticated user should be blocked from seeing the register page again
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage,self).get( *args, **kwargs)
    
    
class TaskList(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = 'tasks' #to give alternate name for object

    def get_context_data(self, **kwargs): #filter based on the user
        context= super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user = self.request.user)
        context['count'] = context['tasks'].filter(complete = False).count()
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__startswith=search_input)
        context['search_input'] = search_input #set the value in the form while rendering the page again
        return context
    
    
class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    template_name = 'base/psg.html' #to give alternate name
    
class CreateTask(LoginRequiredMixin,CreateView):
    model = Task
    fields = ['title','description','complete']
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form): #task will be created based on the user.. no need for drop down in user form fields
        form.instance.user = self.request.user
        return super(CreateTask,self).form_valid(form)
    
class UpdateTask(LoginRequiredMixin,UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    
class DeleteTask(LoginRequiredMixin,DeleteView):
    model= Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')