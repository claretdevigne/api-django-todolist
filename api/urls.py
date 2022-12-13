from django.urls import path
from .views import Authenticate, Register, TasksManager, UpdateTasks

urlpatterns = [
    path('authenticate/', Authenticate.as_view()),
    path('register/', Register.as_view()),
    path('manage/e=<str:email>', TasksManager.as_view()),
    path('update/', UpdateTasks.as_view()),

]