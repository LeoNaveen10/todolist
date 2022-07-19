from django.urls import URLPattern, path
from .views import TaskList,TaskDetail,CreateTask


urlpatterns = [
    
    path('',TaskList.as_view(), name='tasks') ,
    path('task/<int:pk>/',TaskDetail.as_view(),name='task'),   
    path('create-task',CreateTask.as_view(), name='create-task') ,

]