# Generated by Django 3.2.23 on 2024-03-06 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Epharma', '0003_auto_20240306_1152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='Housename',
        ),
        migrations.RemoveField(
            model_name='user',
            name='pin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='place',
        ),
        migrations.RemoveField(
            model_name='user',
            name='post',
        ),
    ]
