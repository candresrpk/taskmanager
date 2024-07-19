from django.urls import path
from .views import tasksView, createTaskView, editTaskView, deleteTaskView

app_name = 'tasks'


urlpatterns = [
    path('', tasksView, name='tasks'),
    path('create/', createTaskView, name='create_tasks'),
    path('edit/<int:id>/', editTaskView, name='edit_task'),
    path('delete/<int:id>/', deleteTaskView, name='delete_task'),
    
]
