from django.http.response import HttpResponsePermanentRedirect
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.views.generic import ListView
from .models import *
from .forms import *
# Create your views here.


# class TaskLlst(ListView):
#     model = Task
#     tasks = Task.objects.all()
#     template_name='index.html'
#     context = {'tasks':tasks,}


def listtask(request):
    tasks = Task.objects.all()
    form = TaskForm
    # if request.method=='POST':
    #     if is_valid():

    return render(request, 'index.html', context={
        'tasks':tasks,
        'form': form,
    })
def createTask(request):
    if request.method=="POST":
        form = TaskForm(request.POST)
        print(form)
        if form.is_valid():
            print(form)
            form.save()
            return redirect('index.html')
    else:
        form = TaskForm()
        print(form)
    return render(request, 'index.html', context={
                'form':form,
            })
