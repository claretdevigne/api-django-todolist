from rest_framework import serializers
from .models import TaskListDatabase, Users

class TasksListSerializers(serializers.ModelSerializer):
    class Meta:
        model = TaskListDatabase
        fields = '__all__'

class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'