# Generated by Django 4.2.7 on 2024-07-25 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManagerApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='ManagerReg_Status',
            field=models.TextField(default='Pending'),
        ),
    ]
