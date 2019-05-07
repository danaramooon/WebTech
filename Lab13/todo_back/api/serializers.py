from rest_framework import serializers
from .models import Task,TaskList
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ('id','username','email','password')

    def create(self, validated_data):
        user = User(
            email = validated_data['email'],
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user

class TaskListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    owner = UserModelSerializer(read_only=True)

    def create(self, validated_data):
        task = TaskList(**validated_data)
        task.save()
        return task

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class TaskModelSerializer(serializers.ModelSerializer):
    task_list = TaskListSerializer(read_only=True)
    owner = UserModelSerializer(read_only=True)
    class Meta:
        model = Task
        fields = ('id', 'name','created_at','due_on','status','task_list','owner')


