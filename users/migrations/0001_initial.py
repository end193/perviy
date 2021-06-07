# Generated by Django 3.2.4 on 2021-06-07 05:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('landing', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=10000, verbose_name='Текст')),
                ('phone_number', models.CharField(max_length=12, verbose_name='Телефон')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Заказчик')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing.servicesmodel', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'Заказ пользователя',
                'verbose_name_plural': 'Заказы пользователей',
                'ordering': ['-date'],
            },
        ),
    ]
