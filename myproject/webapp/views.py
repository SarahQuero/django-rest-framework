from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import employees
from . serializers import employeesSerializer
from rest_framework.decorators import api_view

# Create your views here.

class employeeList(APIView):

    def get(self, request):
        employees1 = employees.objects.all()
        serializer = employeesSerializer(employees1, many= True)
        return Response(serializer.data)

@api_view(['POST'])
def employee(request):
    serializer = employeesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def employee_update(request, pk):
    print ("ici")
    """
    Update a code employee.
    """
    try:
        employee = employees.objects.get(id=pk)
    except employees.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = SnippetSerializer(snippet, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)