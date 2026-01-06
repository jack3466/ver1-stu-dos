from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'subject']
        # Let's add some styling so the input boxes look good
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'What needs to be done?', 'style': 'width: 100%; padding: 10px;'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject (e.g. Math)', 'style': 'width: 100%; padding: 10px;'}),
        }