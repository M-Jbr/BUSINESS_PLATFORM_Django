# Generated by Django 4.1.7 on 2023-02-26 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_alter_orders_send_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='send_to',
            field=models.CharField(default=0, max_length=1000),
        ),
    ]
