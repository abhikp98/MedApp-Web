# Generated by Django 3.2.23 on 2024-03-06 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Epharma', '0002_remove_cart_pharmacy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='longitude',
        ),
        migrations.CreateModel(
            name='address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Housename', models.CharField(max_length=200)),
                ('place', models.CharField(max_length=200)),
                ('post', models.CharField(max_length=200)),
                ('pin', models.BigIntegerField()),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Epharma.user')),
            ],
        ),
        migrations.AddField(
            model_name='purchase',
            name='ADDRESS',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Epharma.address'),
            preserve_default=False,
        ),
    ]