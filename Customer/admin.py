from django.contrib import admin
from Customer.models import *
# Register your models here.

admin.site.register(Customer)
admin.site.register(CustomerRequest)
admin.site.register(Bill)
admin.site.register(BillDetails)



