
from django.shortcuts import get_object_or_404
from Medicine.models import *
from Medicine.serializer import *

# rest framework libraries
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated




from django.shortcuts import render

# Create your views here.



class MedicinneAPIViews(viewsets.ViewSet):

    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    def list(self, request):
        queryset = Medicine.objects.all()
        serializer = MedicineSerializer(queryset, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = MedicineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        queryset = Medicine.objects.all()
        medicine_obj = get_object_or_404(queryset, pk=pk)
        serializer = MedicineSerializer(medicine_obj)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


    def put(self, request, pk=None):
        queryset = Medicine.objects.all()
        medicine_obj = get_object_or_404(queryset, pk=pk)
        serializer = MedicineSerializer(medicine_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk=None):
        try:
            queryset = Medicine.objects.all()
            medicine_obj = get_object_or_404(queryset, pk=pk)
            medicine_obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as error:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)







class MedicineDetailsAPIViews(viewsets.ViewSet):

    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    def list(self, request):
        queryset = MedicineDetails.objects.all()
        serializer = MedicineDetailsSerializer(queryset, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = MedicineDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        queryset = MedicineDetails.objects.all()
        medicine_details_obj = get_object_or_404(queryset, pk=pk)
        serializer = MedicineDetailsSerializer(medicine_details_obj)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


    def put(self, request, pk=None):
        queryset = MedicineDetails.objects.all()
        medicine_details_obj = get_object_or_404(queryset, pk=pk)
        serializer = MedicineDetailsSerializer(medicine_details_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk=None):
        try:
            queryset = MedicineDetails.objects.all()
            medicine_details_obj = get_object_or_404(queryset, pk=pk)
            medicine_details_obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as error:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)


