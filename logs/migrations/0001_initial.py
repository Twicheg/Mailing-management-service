# Generated by Django 4.2.4 on 2023-09-23 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='время попытки')),
                ('status', models.BooleanField(blank=True, default=False, null=True, verbose_name='статус попытки')),
                ('answer', models.TextField(blank=True, null=True, verbose_name='ответ сервиса')),
                ('newsletter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='newsletter.messagesettings', verbose_name='рассылка')),
            ],
            options={
                'verbose_name': 'Лог',
                'verbose_name_plural': 'Логи',
            },
        ),
    ]
