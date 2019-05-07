from django.shortcuts import render
from api.serializers import TaskModelSerializer,TaskListSerializer
from api.models import Task,TaskList
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET','POST'])
def get_tasks(request,id):
    try:
        list = TaskList.objects.get(pk=id)
    except Exception as e:
        return Response({'error': str(e)}, status=404)
    if request.method == "GET":
        task = list.tasks.all()
        serializer = TaskModelSerializer(task,many = True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = TaskModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(task_list = list,owner = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def get_task_list(request):
    if request.method == "GET":
        task = TaskList.objects.all()
        serializer = TaskListSerializer(task,many = True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = TaskListSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def task_detail(request,id):
    try:
        task = Task.objects.get(pk=id)
    except Exception as e:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TaskModelSerializer(task)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = TaskModelSerializer(instance=task,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','PUT','DELETE'])
def list_detail(request,id):
    try:
        task = TaskList.objects.get(pk=id)
    except Exception as e:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TaskListSerializer(task)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = TaskListSerializer(instance=task,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
