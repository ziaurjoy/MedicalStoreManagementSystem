from rest_framework import serializers
from Customer.models import *


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class CustomerRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerRequest
        fields = '__all__'


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'

    # ForeignKey For Company Class
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['customer'] = CustomerSerializer(instance.customer).data
        return response



class BillDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillDetails
        fields = '__all__'

    # ForeignKey For Company Class
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['bill'] = CustomerSerializer(instance.bill.customer).data
        return response
