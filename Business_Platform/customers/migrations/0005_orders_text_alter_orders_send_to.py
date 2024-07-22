# Generated by Django 4.1.7 on 2023-02-26 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_provider_provider_user_delete_customers'),
        ('customers', '0004_alter_orders_send_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='text',
            field=models.CharField(default=0, max_length=1000),
        ),
        migrations.AlterField(
            model_name='orders',
            name='send_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.provider'),
        ),
    ]
