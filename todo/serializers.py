from .models import ToDo
from rest_framework import serializers


class ToDoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ToDo
        fields = ("author","task_title","task_details")