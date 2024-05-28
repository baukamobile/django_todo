from django.shortcuts import render
from django.views.generic import ListView
from .models import *
# Create your views here.


# class TaskLlst(ListView):
#     model = Task
#     tasks = Task.objects.all()
#     template_name='index.html'
#     context = {'tasks':tasks,}


def listtask(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', context={
        'tasks':tasks,
    })