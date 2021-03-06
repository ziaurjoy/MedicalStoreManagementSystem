# Generated by Django 3.1.7 on 2021-03-12 08:35

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('medical_type', models.CharField(max_length=100)),
                ('buy_price', models.CharField(max_length=100)),
                ('sell_price', models.CharField(max_length=100)),
                ('c_gst', models.CharField(max_length=100)),
                ('s_gst', models.CharField(max_length=100)),
                ('batch_no', models.CharField(max_length=100)),
                ('shelf_no', models.CharField(max_length=100)),
                ('exp_date', models.DateField()),
                ('mfg_date', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('in_stock_total', models.IntegerField()),
                ('qty_in_strip', models.CharField(max_length=100)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company.company')),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='MedicineDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salt_name', models.CharField(max_length=100)),
                ('salt_qty', models.CharField(max_length=100)),
                ('desciption', models.TextField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Medicine.medicine')),
            ],
        ),
    ]
