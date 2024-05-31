from django.contrib.admin.utils import reverse
from django.http.response import HttpResponsePermanentRedirect
from django.shortcuts import redirect, render, HttpResponseRedirect, get_object_or_404
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


    return render(request, 'index.html', context={
        'tasks':tasks,
        'form': form,
    })

def detail_view(request, id):
    # context ={}
    data = Task.objects.get(id = id)
    return render(request, "details.html", context={'data':data})

def createTask(request):
    form = TaskForm(request.POST or None)
    context={
        'form':form,
    }
    if form.is_valid():
        form.save()
        return redirect(reverse('listtask'))
    else:
        return render(request,'index.html', context=context)


def update_view(request, id):
    obj = get_object_or_404(Task, id=id)
    form = TaskForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(reverse('detail', args=[id]))
    return render(request, 'update.html', context={
        'task': obj,
        'form': form,
    })
