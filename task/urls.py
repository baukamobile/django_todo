from django.urls import path

from task.views import createTask, detail_view, listtask, update_view


urlpatterns = [
    # path('', TaskLlst.as_view(),name='tasklist'),
    path('', listtask,name='listtask'),
    path('create/', createTask, name='createtask'),
    path('<int:id>/', detail_view, name='detail'),
    path('<int:id>/update/', update_view, name='update'),

]
