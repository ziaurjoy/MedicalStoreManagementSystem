# Generated by Django 3.1.7 on 2021-03-12 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyaccount',
            name='transaction_type',
            field=models.CharField(choices=[('debit', 'Debit'), ('credit', 'Credit')], max_length=20),
        ),
    ]
