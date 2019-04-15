from django.urls import path
from . import views

urlpatterns = [
    path('task_lists/',views.get_task_list),
    path('task_lists/<int:id>/',views.list_detail),
    path('task_lists/<int:id>/tasks/',views.get_tasks),
    path('task/<int:id>/',views.task_detail),
]