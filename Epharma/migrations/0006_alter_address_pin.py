# Generated by Django 3.2.23 on 2024-03-08 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Epharma', '0005_complaints'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='pin',
            field=models.CharField(max_length=200),
        ),
    ]