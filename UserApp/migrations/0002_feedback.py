# Generated by Django 5.0.3 on 2024-07-14 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Feedback_Name', models.CharField(max_length=30)),
                ('Feedback_Email', models.EmailField(max_length=254)),
                ('Feedback_Subject', models.CharField(max_length=30)),
                ('Feedback_Message', models.CharField(max_length=60)),
            ],
        ),
    ]
