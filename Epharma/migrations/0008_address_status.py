# Generated by Django 3.2.23 on 2024-03-12 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Epharma', '0007_remove_purchase_delievery'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='status',
            field=models.CharField(default='active', max_length=100),
        ),
    ]
