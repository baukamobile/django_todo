from django.contrib.admin.utils import reverse
from django.http.response import HttpResponsePermanentRedirect
from django.shortcuts import redirect, render, HttpResponseRedirect, get_object_or_404
from django.views.generic import ListView
from rest_framework import permissions, serializers
from rest_framework import viewsets

from task.serializers import TaskSerializer
from .models import *
from .forms import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
# Create your views here.


# class TaskLlst(ListView):
#     model = Task
#     tasks = Task.objects.all()
#     template_name='index.html'
#     context = {'tasks':tasks,}
#
#
<<<<<<< HEAD




=======
<<<<<<< HEAD
>>>>>>> 914a174 (nothing)
class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


=======



class ListViewtaskSet(ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]
>>>>>>> 5165947 (some problems)


# >>>>>>> 5165947 (some problems)

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
class CreateSomeTasks(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes= [IsAuthenticated]
    serializer_class = TaskSerializer
    @action(detail=False, methods=['post'])
    def createTask(request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect(reverse('listtask'))
        else:
            return render(request,'index.html',)


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


def logIn(request):
    return render(request, 'login.html')
def register(request):
    return render(request, 'register.html')

