from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .serializers import TaskListSerializer,TaskModelSerializer
from .models import Task,TaskList
from django.http import JsonResponse
import json

@csrf_exempt
def get_tasks(request,id):
    try:
        list = TaskList.objects.get(pk=id)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=404)
    if request.method == "GET":
        task = list.tasks.all()
        serializer = TaskModelSerializer(task,many = True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == "POST":
        data = json.loads(request.body)
        serializer = TaskModelSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'error':"invalid data"})

@csrf_exempt
def get_task_list(request):
    if request.method == "GET":
        task = TaskList.objects.all()
        serializer = TaskListSerializer(task,many = True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == "POST":
        data = json.loads(request.body)
        serializer = TaskListSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'error':"invalid data"})

@csrf_exempt
def task_detail(request,id):
    try:
        task = Task.objects.get(pk=id)
    except Exception as e:
        return JsonResponse({'Error':str(e)},status = 404)

    if request.method == "GET":
        serializer = TaskModelSerializer(task)
        return JsonResponse(serializer.data)
    elif request.method == "PUT":
        data = json.loads(request.body)
        serializer = TaskModelSerializer(instance=task,data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'error':'invalid data'})
    elif request.method == "DELETE":
        task.delete()
        return JsonResponse({'deleted':True})

@csrf_exempt
def list_detail(request,id):
    try:
        task = TaskList.objects.get(pk=id)
    except Exception as e:
        return JsonResponse({'Error':str(e)},status = 404)

    if request.method == "GET":
        serializer = TaskListSerializer(task)
        return JsonResponse(serializer.data)
    elif request.method == "PUT":
        data = json.loads(request.body)
        serializer = TaskListSerializer(instance=task,data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'error':'invalid data'})
    elif request.method == "DELETE":
        task.delete()
        return JsonResponse({'deleted':True})

#
# def get_task_list(request):
#     task_list = TaskList.objects.all()
#     task_list = [t.to_json() for t in task_list]
#     return JsonResponse(task_list,safe=False)
#
# def list_detail(request,id):
#     try:
#         list = TaskList.objects.get(pk=id)
#     except Exception as e:
#         return JsonResponse({'error':str(e)},status=404)
#     return JsonResponse(list.to_json())
#
# def get_tasks(request,id):
#     try:
#         list = TaskList.objects.get(pk=id)
#     except Exception as e:
#         return JsonResponse({'error':str(e)},status=404)
#     task = list.tasks.all()
#     task = [t.to_json() for t in task]
#     return JsonResponse(task,safe=False)
#
# def task_detail(request,id):
#     try:
#         list = Task.objects.get(pk=id)
#     except Exception as e:
#         return JsonResponse({'error':str(e)},status=404)
#     return JsonResponse(list.to_all_json())
