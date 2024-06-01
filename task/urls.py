from django.urls import path

from task.views import delete_view, detail_view, listtask, logIn, register, submitting_view, update_view, CreateSomeTasks
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
# router.register(r'task',TaskViewSet)


urlpatterns = [

    path('', listtask,name='listtask'),
    # path('serializing/', TaskViewSet.as_view,name='tasklist'),,
    # path('create/', createTask, name='createtask'),
    path('create/', CreateSomeTasks.as_view({'post': 'createTask'}),name='createtask'),
    path('<int:id>/details/', detail_view, name='detail'),
    path('<int:id>/', update_view, name='update'),
    path('<int:id>/delete/', delete_view, name='delete'),
    path('<int:id>/submitting/', submitting_view, name='submitting'),
    path('login/', logIn, name='login'),
    path('register/', register, name='register'),


]
# urlpatterns += router.urls
