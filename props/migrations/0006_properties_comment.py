# Generated by Django 4.1.4 on 2023-03-01 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('props', '0005_rename_property_id_propertycomment_property'),
    ]

    operations = [
        migrations.AddField(
            model_name='properties',
            name='comment',
            field=models.TextField(blank=True, db_column='Comment', null=True),
        ),
    ]
