from django import forms

from .models import Tarefa

class TaskForm(forms.ModelForm):

    class Meta:
        model = Tarefa
        fields = ('titulo', 'descricao', 'setor')