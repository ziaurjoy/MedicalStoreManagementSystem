from django.db import models
from Medicine.models import *
# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact = models.CharField(max_length=15)
    added_on = models.DateTimeField(auto_now_add=True)


class CustomerRequest(models.Model):
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    medicine_details = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now_add=True)


class Bill(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    added_on = models.DateField(auto_now_add=True)


class BillDetails(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    medical_id = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    qty = models.IntegerField()
    added_on = models.DateTimeField(auto_now_add=True)
