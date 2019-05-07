from django.db import models
from django.contrib.auth.models import User

class TaskListManager(models.Manager):
    def for_user(self, user):
        return self.filter(owner=user)

class TaskList(models.Model):
    name = models.CharField(max_length=100);
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    objects = TaskListManager()
    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'id':self.id,
            'name': self.name
        }

class Task(models.Model):
    name = models.CharField(max_length=100);
    created_at = models.DateTimeField(auto_now_add=True);
    due_on = models.DateTimeField();
    status = models.CharField(max_length=100);
    task_list = models.ForeignKey(TaskList,on_delete=models.CASCADE,related_name="tasks");
    owner = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'id':self.id,
            'name': self.name,
            'status':self.status
        }
    def to_all_json(self):
        return {
            'id':self.id,
            'name': self.name,
            'created_at':self.created_at,
            'status':self.status,
            'due_on': self.due_on,
            'task_list':self.task_list.name
        }