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

    @staticmethod
    def getEmployee(active):
        employees1 = employees.objects.exclude(active=active)
        serializer = employeesSerializer(employees1, many= True)
        return Response(serializer.data)

    def get(self, request):
        return employeeList.getEmployee(False)
    
    def post(self, request):
        serializer = employeesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class employeeDeleteList(APIView):

    def get(self, request):
        return employeeList.getEmployee(True)

class employeeDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return employees.objects.get(pk=pk)
        except employees.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = employeesSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = employeesSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        print('Hello')
        employee = self.get_object(pk)
        # Modify the active field to turn it to false value
        employee.active = False
        # Save the modification 
        employee.save()
        # employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
