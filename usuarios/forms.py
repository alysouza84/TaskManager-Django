from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status']
        
class TaskFilterForm(forms.Form):
    status = forms.ChoiceField(
        choices=[('', 'Todos')] + Task.STATUS_CHOICES,
        required=False,
        label='Filtrar por status'
    )