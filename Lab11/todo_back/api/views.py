from django.shortcuts import render
from django.http import JsonResponse
from .models import TaskList,Task
# Create your views here.

def get_task_list(request):
    task_list = TaskList.objects.all()
    task_list = [t.to_json() for t in task_list]
    return JsonResponse(task_list,safe=False)

def list_detail(request,id):
    try:
        list = TaskList.objects.get(pk=id)
    except Exception as e:
        return JsonResponse({'error':str(e)},status=404)
    return JsonResponse(list.to_json())

def get_tasks(request,id):
    try:
        list = TaskList.objects.get(pk=id)
    except Exception as e:
        return JsonResponse({'error':str(e)},status=404)
    task = list.tasks.all()
    task = [t.to_all_json() for t in task]
    return JsonResponse(task,safe=False)

def task_detail(request,id):
    try:
        list = Task.objects.get(pk=id)
    except Exception as e:
        return JsonResponse({'error':str(e)},status=404)
    return JsonResponse(list.to_all_json())
