from rest_framework import serializers
from Medicine.models import *


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'



class MedicineDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineDetails
        fields = '__all__'

    # ForeignKey For Company Class
    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     response['company_name'] = MedicineSerializer(instance.medicine).data
    #     return response