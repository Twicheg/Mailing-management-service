# Generated by Django 4.2.4 on 2023-09-24 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='number_of_views',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='количество просмотров'),
        ),
    ]
