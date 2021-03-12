

from django.shortcuts import render
# import Project Module
from Company.models import Company
from Company.serializer import CompanySerializer

# import rest_framework Module
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated






# Company list API
class CompanyList(APIView):
    def get(self, request, format=None):
        snippets = Company.objects.all()
        company = CompanySerializer(snippets, many=True)
        return Response(company.data)


# Company Create API
class CompanyCreate(APIView):

    # Authentication Check API
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        persions_serializer = CompanySerializer(data=request.data)
        if persions_serializer.is_valid():
            persions_serializer.save()
            return Response(persions_serializer.data, status=status.HTTP_201_CREATED)
        return Response(persions_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Update Delete API
class CompanyUpdate(APIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_persion(self, id):
        try:
            return Company.objects.get(id=id)
        except Company.DoesNotExist:
            Response(Company.errors, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id, format=None):
        persion = self.get_persion(id)
        persion_serializer = CompanySerializer(persion)
        return Response(persion_serializer.data)

    def put(self, request, id, format=None):
        persion = self.get_persion(id)
        persion_serializer = CompanySerializer(persion, data=request.data)
        if persion_serializer.is_valid():
            persion_serializer.save()
            return Response(persion_serializer.data)
        return Response(persion_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        persion = self.get_persion(id)
        persion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)