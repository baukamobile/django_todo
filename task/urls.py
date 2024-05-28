from django.urls import path

from task.views import TaskLlst


urlpatterns = [
    path('', TaskLlst.as_view(),name='tasklist'),

]
