# Generated by Django 3.2.6 on 2021-08-11 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_orders_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]
