from django.urls import path

<<<<<<< HEAD
from task.views import delete_view, detail_view, listtask, logIn, register, submitting_view, update_view, CreateSomeTasks
=======
from task.views import ListViewtaskSet, createTask, delete_view, detail_view, listtask, submitting_view, update_view
>>>>>>> 914a174 (nothing)
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
# router.register(r'task',TaskViewSet)


urlpatterns = [
<<<<<<< HEAD

=======
>>>>>>> 5165947 (some problems)
    path('', listtask,name='listtask'),
<<<<<<< HEAD
    # path('serializing/', TaskViewSet.as_view,name='tasklist'),,
    # path('create/', createTask, name='createtask'),
    path('create/', CreateSomeTasks.as_view({'post': 'createTask'}),name='createtask'),
=======
    # path('serializing/', TaskViewSet.as_view,name='tasklist'),
    path('alltask/', ListViewtaskSet,name='all'),
    path('create/', createTask, name='createtask'),

>>>>>>> 914a174 (nothing)
    path('<int:id>/details/', detail_view, name='detail'),
    path('<int:id>/', update_view, name='update'),
    path('<int:id>/delete/', delete_view, name='delete'),
    path('<int:id>/submitting/', submitting_view, name='submitting'),
    path('login/', logIn, name='login'),
    path('register/', register, name='register'),


]
# urlpatterns += router.urls
