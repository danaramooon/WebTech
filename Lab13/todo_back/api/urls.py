from django.urls import path
from .views import fbv,auth_,cbv

urlpatterns = [
    path('task_lists/',fbv.get_task_list),
    path('cbv/task_lists/',cbv.TaskListView.as_view()),
    path('cbv/task_lists/create',cbv.TaskListCreateView.as_view()),
     path('cbv/task_lists/<int:pk>/',cbv.TaskListUpdateView.as_view()),
    path('cbv/task_lists/create/',cbv.TaskListCreateView.as_view()),
    path('task_lists/<int:id>/',fbv.list_detail),
    path('task_lists/<int:id>/tasks/',fbv.get_tasks),
    path('cbv/task_lists/<int:pk>/tasks/create/',cbv.TaskCreateView.as_view()),
    path('task/<int:id>/',fbv.task_detail),
    path('login/',auth_.login),
    path('register/',auth_.register),
    path('logout/',auth_.logout),

]