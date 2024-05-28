from django.urls import path

from task.views import listtask


urlpatterns = [
    # path('', TaskLlst.as_view(),name='tasklist'),
    path('', listtask,name='listtask'),

]
