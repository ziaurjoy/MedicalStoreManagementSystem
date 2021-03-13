
from rest_framework import serializers
from Company.models import *


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'




class CompanyAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyAccount
        fields = '__all__'

    # ForeignKey For Company Class
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['company'] = CompanySerializer(instance.company).data
        return response





class CompanyBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyBank
        fields = '__all__'

    # ForeignKey For Company Class
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['company'] = CompanySerializer(instance.company).data
        return response




