from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'user']
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.instance.user = user # Define o usuário atual como o usuário da tarefa

class TaskFilterForm(forms.Form):
    status = forms.ChoiceField(
        choices=[('', 'Todos')] + Task.STATUS_CHOICES,
        required=False,
        label='Filtrar por status'
    )
