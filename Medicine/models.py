from django.db import models
from Company.models import *
# Create your models here.




# MEDICINE
class Medicine(models.Model):
    name = models.CharField(max_length=100)
    medical_type = models.CharField(max_length=100)
    buy_price = models.CharField(max_length=100)
    sell_price = models.CharField(max_length=100)
    c_gst = models.CharField(max_length=100)
    s_gst = models.CharField(max_length=100)
    batch_no = models.CharField(max_length=100)
    shelf_no = models.CharField(max_length=100)
    exp_date = models.DateField()
    mfg_date = models.CharField(max_length=100)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    in_stock_total = models.IntegerField()
    qty_in_strip = models.CharField(max_length=100)
    added_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name




class MedicineDetails(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    salt_name = models.CharField(max_length=100)
    salt_qty = models.CharField(max_length=100)
    desciption = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.medicine)