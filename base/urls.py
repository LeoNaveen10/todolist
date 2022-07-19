from django.urls import URLPattern, path
from .views import TaskList,TaskDetail,CreateTask,UpdateTask,DeleteTask,CustomLogin
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('login/',CustomLogin.as_view(), name='login') ,
    path('logout/',LogoutView.as_view(next_page = 'login'), name='logout') ,
    path('',TaskList.as_view(), name='tasks') ,
    path('task/<int:pk>/',TaskDetail.as_view(),name='task'),   
    path('create-task/',CreateTask.as_view(), name='create-task') ,
    path('edit-task/<int:pk>/',UpdateTask.as_view(), name='update-task'),
    path('delete-task/<int:pk>/',DeleteTask.as_view(), name='delete-task'),

]