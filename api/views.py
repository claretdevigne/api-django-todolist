from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .serializer import UsersSerializers
from .models import Users
from rest_framework import status

class Authenticate(APIView):

    @method_decorator(csrf_exempt) 
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, format=None):
        email = request.data['email']
        password = request.data['password']
        user = Users.objects.filter(user=email)
        
        if len(user) == 1:
            user = Users.objects.filter(user=email)
            passwordTMP = user.values()[0]['password']
            if password == passwordTMP:
                # username = f"{user.values()[0]['name']} {user.values()[0]['lastname']}"
                # useremail = user.values()[0]['user']
                # startdate = user.values()[0]['startdate']
                # data = [{"user": username, "email": useremail, "startdate": startdate}]
                return Response( status = 200)
            else:
                return Response(status = 401)
        elif len(user) == 0:
            return Response(status = 404)

class Register(APIView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, format=None):
        
        userValidation = Users.objects.filter(user=request.data['email'])
        if len(userValidation) > 0:
            return Response(status=status.HTTP_302_FOUND)
        else:
            Users.objects.create(
                user = request.data['email'],
                password = request.data['password'],
                name = request.data['name'].title(),
                lastname = request.data['lastname'].title(),
                data = '[]',
            )
            return Response(status=status.HTTP_201_CREATED)

class TasksManager(APIView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, email, format=None):
        user = Users.objects.filter(user=email)
        serializers = UsersSerializers(user, many=True)        
        return Response(serializers.data, status=status.HTTP_200_OK)

class UpdateTasks(APIView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def put(self, request, format=None):
        email = request.data['email']
        data = request.data['data']
        user = Users.objects.filter(user=email)
        user.update(
            data = data
        )
        return Response(status=status.HTTP_200_OK)