# Generated by Django 4.2.4 on 2023-09-24 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_clients_content_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='content_creator',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='создатель клиента'),
        ),
    ]