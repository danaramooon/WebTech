from django.db import models

class TaskList(models.Model):
    name = models.CharField(max_length=100);

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