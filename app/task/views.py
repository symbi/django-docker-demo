from django.shortcuts import render

from .models import Task
from .serializers import TaskSerializer

from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# def TaskViewSet(request):
# 	print("task view set")
# 	return render(request, 'test.html')
class TaskViewSet(viewsets.ModelViewSet):
	#print("task view set")
    #authentication_classes = (BasicAuthentication,)
    #permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


def sakura(request):
    return render(request, 'test.html')