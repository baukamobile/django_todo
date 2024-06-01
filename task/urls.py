from django.urls import path

from task.views import ListViewtaskSet, createTask, delete_view, detail_view, listtask, submitting_view, update_view
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
# router.register(r'task',TaskViewSet)


urlpatterns = [
<<<<<<< HEAD
=======
<<<<<<< HEAD

=======
>>>>>>> 5165947 (some problems)
>>>>>>> 914a174
    path('', listtask,name='listtask'),
    # path('serializing/', TaskViewSet.as_view,name='tasklist'),
    path('alltask/', ListViewtaskSet,name='all'),
    path('create/', createTask, name='createtask'),

    path('<int:id>/details/', detail_view, name='detail'),
    path('<int:id>/', update_view, name='update'),
    path('<int:id>/delete/', delete_view, name='delete'),
    path('<int:id>/submitting/', submitting_view, name='submitting'),


]
# urlpatterns += router.urls
