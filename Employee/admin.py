from django.contrib import admin
from Employee.models import *
# Register your models here.

admin.site.register(Employee)
admin.site.register(EmployeeBank)
admin.site.register(EmployeeSalary)