# Generated by Django 4.0.6 on 2022-09-19 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomtypes',
            name='pictureurl',
        ),
    ]
