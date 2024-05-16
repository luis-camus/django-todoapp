from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['name', 'priority', 'done']
        
    def __init__(self, *args, **kwargs):
        # Get the user from the kwargs (if provided)
        request = kwargs.pop('request', None)
        super(TodoForm, self).__init__(*args, **kwargs)

        # Store the user ID as an instance variable
        self.user_id = request.user.id

    def save(self, commit=True):
        # Set the user ID for the Todo instance
        todo = super().save(commit=False)
        todo.user_id = self.user_id

        if commit:
            todo.save()

        return todo