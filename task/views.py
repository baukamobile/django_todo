from django.contrib.admin.utils import reverse
from django.http.response import HttpResponsePermanentRedirect
from django.shortcuts import redirect, render, HttpResponseRedirect, get_object_or_404
from django.views.generic import ListView
from rest_framework import permissions

from task.serializers import TaskSerializer
from .models import *
from .forms import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
# Create your views here.


# class TaskLlst(ListView):
#     model = Task
#     tasks = Task.objects.all()
#     template_name='index.html'
#     context = {'tasks':tasks,}
#
#
class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer



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
        return redirect(reverse('listtask'))  # Assuming 'createtask' is the correct URL
    return render(request, 'update.html', context={'obj': obj, 'form': form})

def delete_view(request, id):
    obj_del = get_object_or_404(Task, id=id)
    obj_del.delete()
    return redirect(reverse('listtask'), context={
        'obj_del':obj_del,
    })
def submitting_view(request, id):
    submitting = Task.objects.get(request, id)
    form = TaskForm(request.POST or None, instance=submitting)
    if form.is_valid():
        form.save()
        return redirect(reverse('listtask'))  # Assuming 'createtask' is the correct URL
    return render(request, 'index.html', context={'submitting': submitting, 'form': form})
