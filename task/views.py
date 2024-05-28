from django.shortcuts import render
from django.views.generic import ListView
from .models import * 
# Create your views here.


class TaskLlst(ListView):
    model = Task
    template_name='index.html'


