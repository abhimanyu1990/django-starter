

from django.db import models
from user.models import User

class ToDo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    task_title = models.CharField(max_length=200)
    task_details = models.TextField()
    def __str__(self):
        return self.title