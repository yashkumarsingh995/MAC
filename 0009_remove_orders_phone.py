# Generated by Django 3.2.6 on 2021-08-11 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_orders_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='phone',
        ),
    ]