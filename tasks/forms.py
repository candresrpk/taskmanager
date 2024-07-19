from django.forms import ModelForm
from .models import Task

class CreateTasksForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
        

class EditTasksForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status']