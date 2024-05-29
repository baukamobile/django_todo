from django.urls import path

from task.views import createTask, listtask


urlpatterns = [
    # path('', TaskLlst.as_view(),name='tasklist'),
    path('', listtask,name='listtask'),
    path('create/', createTask, name='createtask'),

]
