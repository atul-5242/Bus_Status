# Generated by Django 4.1.3 on 2023-01-26 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup_student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentdetails',
            name='Id',
        ),
    ]
