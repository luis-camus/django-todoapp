from django import forms
from .models import todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = todo
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add a new task'})
        }