# Generated by Django 3.1.7 on 2021-03-13 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billdetails',
            old_name='medical_id',
            new_name='medicine',
        ),
    ]
