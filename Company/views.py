
from django.shortcuts import get_object_or_404
from Company.models import *
from Company.serializer import *

# rest framework libraries
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated






class CompanyAPIViews(viewsets.ViewSet):

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def list(self, request):
        queryset = Company.objects.all()
        serializer = CompanySerializer(queryset, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def retrieve(self, request, pk=None):
        queryset = Company.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = CompanySerializer(user)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)



    def put(self, request, pk, format=None):
        queryset = Company.objects.all()
        company_obj = get_object_or_404(queryset, pk=pk)
        serializer = CompanySerializer(company_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, pk=None):
        try:
            queryset = Company.objects.all()
            company_obj = get_object_or_404(queryset, pk=pk)
            company_obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as error:
            return Response(error)








class CompanyAccountAPIView(viewsets.ViewSet):

    def list(self, request):
        queryset = CompanyAccount.objects.all()
        serializer = CompanyAccountSerializer(queryset, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = CompanyAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def retrieve(self, request, pk=None):
        queryset = CompanyAccount.objects.all()
        company_account_obj = get_object_or_404(queryset, pk=pk)
        serializer = CompanyAccountSerializer(company_account_obj)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)



    def put(self, request, pk):
        queryset = CompanyAccount.objects.all()
        company_account_obj = get_object_or_404(queryset, pk=pk)
        serializer = CompanyAccountSerializer(company_account_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, pk=None):
        try:
            queryset = CompanyAccount.objects.all()
            company_account_obj = get_object_or_404(queryset, pk=pk)
            company_account_obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as error:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)





