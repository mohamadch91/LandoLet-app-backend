# Generated by Django 4.0.6 on 2022-09-20 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_alter_furnitures_isactive_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='furnituresinroomspictures',
            old_name='url',
            new_name='image',
        ),
    ]