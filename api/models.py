from django.db import models
import uuid

# Create your models here.
class TaskListDatabase(models.Model):

    title = models.CharField(max_length=250)
    deadline = models.DateField()
    manager = models.CharField(max_length=50)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Users(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    user = models.EmailField(unique=True)
    password = models.CharField(max_length=250)
    name = models.CharField(max_length=250, null=True)
    lastname = models.CharField(max_length=250, null=True)
    startdate = models.DateField(auto_now_add=True, null=True)
    data = models.TextField()

    def __str__(self):
        return self.user

