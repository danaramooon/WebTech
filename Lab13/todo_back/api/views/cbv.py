from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from api.serializers import TaskListSerializer,TaskModelSerializer
from api.models import TaskList,Task

from rest_framework import generics

class TaskListView(generics.ListAPIView):
    #queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return TaskList.objects.for_user(self.request.user)


class TaskListCreateView(generics.CreateAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)


class TaskListDetailView(generics.RetrieveAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer

    def get_object(self):
        queryset = TaskList.objects.get(id=self.kwargs["id"])
        return queryset

class TaskListUpdateView(generics.UpdateAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class TaskListDeleteView(generics.DestroyAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def perform_create(self, serializer):
        serializer.save(task_list = TaskList.objects.get(id=self.kwargs["pk"]),owner = self.request.user)






