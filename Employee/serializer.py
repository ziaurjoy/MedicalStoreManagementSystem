from rest_framework import serializers
from Employee.models import *

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeSalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeSalary
        fields = '__all__'

        # ForeignKey For Company Class
        def to_representation(self, instance):
            response = super().to_representation(instance)
            response['employee'] = EmployeeSerializer(instance.employee).data
            return response


class EmployeeBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeBank
        fields = '__all__'