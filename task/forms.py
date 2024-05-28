from django import forms
from .models import *

class TaskForm(forms.ModelForm):
    model = Task
    fields = ['title', 'comment',]