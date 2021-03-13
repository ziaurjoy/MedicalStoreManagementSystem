from django.shortcuts import render


from django.shortcuts import get_object_or_404
from Customer.models import *
from Customer.serializer import *

# rest framework libraries
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.




class CustomerAPIView(viewsets.ViewSet):

    def list(self, request):
        queryset = Customer.objects.all()
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        queryset = Customer.objects.all()
        customer_obj = get_object_or_404(queryset, pk=pk)
        serializer = CustomerSerializer(customer_obj)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


    def put(self, request, pk):
        queryset = Customer.objects.all()
        customer_obj = get_object_or_404(queryset, pk=pk)
        serializer = CustomerSerializer(customer_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk=None):
        try:
            queryset = Customer.objects.all()
            customer_obj = get_object_or_404(queryset, pk=pk)
            customer_obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as error:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)





class CustomerRequestAPIView(viewsets.ViewSet):

    def list(self, request):
        queryset = CustomerRequest.objects.all()
        serializer = CustomerRequestSerializer(queryset, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = CustomerRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        queryset = CustomerRequest.objects.all()
        customer_obj = get_object_or_404(queryset, pk=pk)
        serializer = CustomerRequestSerializer(customer_obj)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


    def put(self, request, pk):
        queryset = CustomerRequest.objects.all()
        customer_obj = get_object_or_404(queryset, pk=pk)
        serializer = CustomerRequestSerializer(customer_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk=None):
        try:
            queryset = CustomerRequest.objects.all()
            customer_obj = get_object_or_404(queryset, pk=pk)
            customer_obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as error:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)






class BillAPIView(viewsets.ViewSet):

    def list(self, request):
        queryset = Bill.objects.all()
        serializer = BillSerializer(queryset, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = BillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        queryset = Bill.objects.all()
        bill_obj = get_object_or_404(queryset, pk=pk)
        serializer = BillSerializer(bill_obj)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


    def put(self, request, pk):
        queryset = Bill.objects.all()
        bill_obj = get_object_or_404(queryset, pk=pk)
        serializer = BillSerializer(bill_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk=None):
        try:
            queryset = Bill.objects.all()
            bill_obj = get_object_or_404(queryset, pk=pk)
            bill_obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as error:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)





class BillDetailsAPIView(viewsets.ViewSet):

    def list(self, request):
        queryset = BillDetails.objects.all()
        serializer = BillDetailsSerializer(queryset, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = BillDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        queryset = BillDetails.objects.all()
        bill_obj = get_object_or_404(queryset, pk=pk)
        serializer = BillDetailsSerializer(bill_obj)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


    def put(self, request, pk):
        queryset = BillDetails.objects.all()
        bill_obj = get_object_or_404(queryset, pk=pk)
        serializer = BillDetailsSerializer(bill_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk=None):
        try:
            queryset = BillDetails.objects.all()
            bill_obj = get_object_or_404(queryset, pk=pk)
            bill_obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as error:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)

