from rest_framework import serializers
from .models import Task,TaskList
from datetime import datetime, timedelta

class TaskListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)

    def create(self, validated_data):
        task = TaskList(**validated_data)
        task.save()
        return task

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class TaskModelSerializer(serializers.ModelSerializer):
    task_list = TaskListSerializer
    class Meta:
        model = Task
        fields = ('id', 'name','created_at','due_on','status','task_list')

