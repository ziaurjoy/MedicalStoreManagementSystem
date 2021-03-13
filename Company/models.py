from django.db import models

# Create your models here.
#COMPANY
class Company(models.Model):
    name = models.CharField(max_length=100)
    license_no = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=14)
    email = models.EmailField()
    description = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CompanyAccount(models.Model):
    choice = (
        ("debit", 'Debit'),
        ('credit', 'Credit')
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    transaction_type = models.CharField(choices=choice, max_length=20)
    transaction_amount = models.CharField(max_length=100)
    transaction_date = models.DateTimeField(auto_now_add=True)
    payment_model = models.CharField(max_length=100)

    def __str__(self):
        return self.company.name



class CompanyBank(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    bank_account_no = models.CharField(max_length=100)
    ifsc = models.CharField(max_length=100)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company.name