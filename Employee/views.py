from django.shortcuts import render
from django.shortcuts import get_object_or_404
from Employee.models import *
from Employee.serializer import *

# rest framework libraries
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status






class EmployeeAPIView(viewsets.ViewSet):

    def list(self, request):
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = EmployeeSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        queryset = Employee.objects.all()
        employee_obj = get_object_or_404(queryset, pk=pk)
        serializer = EmployeeSerializer(employee_obj)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


    def put(self, request, pk):
        queryset = Employee.objects.all()
        employee_obj = get_object_or_404(queryset, pk=pk)
        serializer = EmployeeSerializer(employee_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk=None):
        try:
            queryset = Employee.objects.all()
            employee_obj = get_object_or_404(queryset, pk=pk)
            employee_obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as error:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)





class EmployeeSalaryAPIView(viewsets.ViewSet):

    def list(self, request):
        queryset = EmployeeSalary.objects.all()
        serializer = EmployeeSalarySerializer(queryset, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = EmployeeSalarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        queryset = EmployeeSalary.objects.all()
        employee_obj = get_object_or_404(queryset, pk=pk)
        serializer = EmployeeSalarySerializer(employee_obj)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


    def put(self, request, pk):
        queryset = EmployeeSalary.objects.all()
        employee_obj = get_object_or_404(queryset, pk=pk)
        serializer = EmployeeSalarySerializer(employee_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk=None):
        try:
            queryset = EmployeeSalary.objects.all()
            employee_obj = get_object_or_404(queryset, pk=pk)
            employee_obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as error:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)






class EmployeeBankAPIView(viewsets.ViewSet):

    def list(self, request):
        queryset = EmployeeBank.objects.all()
        serializer = EmployeeBankSerializer(queryset, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = EmployeeBankSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        queryset = EmployeeBank.objects.all()
        employee_obj = get_object_or_404(queryset, pk=pk)
        serializer = EmployeeBankSerializer(employee_obj)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


    def put(self, request, pk):
        queryset = EmployeeBank.objects.all()
        employee_obj = get_object_or_404(queryset, pk=pk)
        serializer = EmployeeBankSerializer(employee_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk=None):
        try:
            queryset = EmployeeBank.objects.all()
            employee_obj = get_object_or_404(queryset, pk=pk)
            employee_obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as error:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
