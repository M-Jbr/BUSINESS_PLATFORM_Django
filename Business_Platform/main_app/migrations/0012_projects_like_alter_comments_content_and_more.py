# Generated by Django 4.1.7 on 2023-02-28 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_customers'),
        ('main_app', '0011_backlog_provider_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='like',
            field=models.ManyToManyField(blank=True, null=True, related_name='projects', to='accounts.customers'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.ImageField(blank=True, default='images/default.jpg', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='rating',
            field=models.FloatField(blank=True, default='5', null=True),
        ),
    ]
